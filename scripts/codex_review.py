# -*- coding: utf-8 -*-
"""Historical static-review launcher, extracted for RelayPilot Gen 1."""
import json, re, subprocess, time, pathlib
from datetime import datetime

# Publication copy: configuration-only extraction of the historical launcher.
# Review parsing and event handling below retain their original limitations.
import argparse, os, shutil, sys

parser = argparse.ArgumentParser(description="Standalone Codex static-review launcher (Preview).")
mode = parser.add_mutually_exclusive_group(required=True)
mode.add_argument("--check", action="store_true", help="Validate config only; no model execution")
mode.add_argument("--execute", action="store_true", help="Opt in to a real potentially paid model call")
args = parser.parse_args()
required = ("CODEX_EXE", "WORK_DIR", "REPO_DIR", "MODEL", "TASK_ID", "REVIEW_COMMIT", "PLAN_SESSION")
missing = [key for key in required if not os.environ.get("RELAYPILOT_" + key)]
if missing:
    parser.error("Missing configuration: " + ", ".join("RELAYPILOT_" + key for key in missing))
CODEX = os.environ["RELAYPILOT_CODEX_EXE"]
PROJ = pathlib.Path(os.environ["RELAYPILOT_WORK_DIR"]).resolve()
REPO = pathlib.Path(os.environ["RELAYPILOT_REPO_DIR"]).resolve()
MODEL = os.environ["RELAYPILOT_MODEL"]
TASK_ID = os.environ["RELAYPILOT_TASK_ID"]
REVIEW_COMMIT = os.environ["RELAYPILOT_REVIEW_COMMIT"]
PLAN_SESSION = os.environ["RELAYPILOT_PLAN_SESSION"]
if not re.fullmatch(r"[0-9a-fA-F]{40}", REVIEW_COMMIT):
    parser.error("Review commit must be a 40-character hexadecimal SHA")
if not re.fullmatch(r"[A-Za-z0-9_-]+", TASK_ID):
    parser.error("Task ID must contain only letters, digits, underscore or hyphen")
try:
    TIMEOUT = int(os.environ.get("RELAYPILOT_TIMEOUT", "120"))
except ValueError:
    parser.error("Timeout must be an integer")
if not 1 <= TIMEOUT <= 120:
    parser.error("Timeout must be between 1 and 120 seconds")
if not PROJ.is_dir() or not REPO.is_dir():
    parser.error("Work and repository directories must already exist")
if not (PROJ / "review-input.txt").is_file():
    parser.error("Missing review-input.txt in work directory")
if not shutil.which(CODEX):
    parser.error("Codex executable not found")
if args.check:
    print("CONFIG_VALID; model execution NOT performed; served_model=UNVERIFIED")
    raise SystemExit(0)

review_input = (PROJ / "review-input.txt").read_text(encoding="utf-8-sig")
instruction = """You are doing an ultra-lean static review for the configured task.
Rules: No tools/shell/file reads/tests/code changes. Use ONLY REVIEW INPUT.
Reply with ONLY one JSON object (no markdown fences):
{"task_id":"TASK_PLACEHOLDER","review_commit":"COMMIT_PLACEHOLDER","decision":"APPROVE or REQUEST_CHANGES","findings":[],"reason":"...","linkage_plan_session":"PLAN_PLACEHOLDER"}

REVIEW INPUT:
"""
instruction = instruction.replace("TASK_PLACEHOLDER", TASK_ID).replace("COMMIT_PLACEHOLDER", REVIEW_COMMIT).replace("PLAN_PLACEHOLDER", PLAN_SESSION)
prompt = instruction + review_input
prompt_bytes = len(prompt.encode("utf-8"))
ts = datetime.now().strftime("%Y%m%d-%H%M%S")
run_dir = PROJ / "review-run" / ts
run_dir.mkdir(parents=True, exist_ok=True)
(run_dir / "prompt.txt").write_text(prompt, encoding="utf-8", newline="\n")
(run_dir / "prompt-bytes.txt").write_text(str(prompt_bytes)+"\n", encoding="utf-8")
last_msg_path = run_dir / "last-message.txt"

cmd = [CODEX, "exec", "-s", "read-only", "-m", MODEL, "-c", 'model_provider="magpie"', "-C", str(REPO), "--json", "-o", str(last_msg_path), "-"]
started = time.time(); timed_out=False; exit_code=-1; stdout_data=""; stderr_data=""
try:
    proc = subprocess.Popen(cmd, cwd=str(REPO), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="replace")
    try:
        stdout_data, stderr_data = proc.communicate(input=prompt, timeout=TIMEOUT)
        exit_code = proc.returncode if proc.returncode is not None else -1
    except subprocess.TimeoutExpired:
        timed_out=True; proc.kill()
        try: stdout_data, stderr_data = proc.communicate(timeout=10)
        except Exception: pass
        exit_code=-1
except Exception as e:
    stderr_data=f"LAUNCH_ERROR: {e}"; exit_code=-2

wall=round(time.time()-started,3)
(run_dir/"stdout.txt").write_text(stdout_data or "", encoding="utf-8")
(run_dir/"stderr.txt").write_text(stderr_data or "", encoding="utf-8")

new_session_id=None; agent_texts=[]
for line in (stdout_data or "").splitlines():
    line=line.strip()
    if not line.startswith("{"): continue
    try: ev=json.loads(line)
    except Exception: continue
    t=ev.get("type") or ev.get("event") or ""
    if t in ("thread.started","session_created","thread_started"):
        tid=ev.get("thread_id") or ev.get("session_id") or (ev.get("thread") or {}).get("id")
        if tid: new_session_id=tid
    if isinstance(ev.get("thread"), dict) and ev["thread"].get("id") and str(t).endswith("started"):
        new_session_id=ev["thread"]["id"]
    item=ev.get("item") or {}
    if isinstance(item, dict) and item.get("type") in ("agent_message","message"):
        txt=item.get("text") or item.get("content") or ""
        if isinstance(txt, list):
            txt="".join((x.get("text") if isinstance(x, dict) else str(x)) for x in txt)
        if txt: agent_texts.append(str(txt))

last_msg=""
if last_msg_path.exists():
    last_msg=last_msg_path.read_text(encoding="utf-8", errors="replace")
    if last_msg.strip(): agent_texts.append(last_msg)
combined="\n".join(agent_texts)+"\n"+(stdout_data or "")
decision_obj=None

def try_parse(s):
    global decision_obj
    s=s.strip()
    if s.startswith("```"):
        s=re.sub(r"^```(?:json)?\s*","",s); s=re.sub(r"\s*```$","",s)
    try:
        obj=json.loads(s)
        if isinstance(obj, dict) and obj.get("decision") in ("APPROVE","REQUEST_CHANGES"):
            decision_obj=obj; return True
    except Exception: pass
    return False

if last_msg and try_parse(last_msg):
    pass
else:
    for m in re.finditer(r"\"decision\"\s*:\s*\"(?:APPROVE|REQUEST_CHANGES)\"", combined):
        brace=combined.rfind("{", 0, m.start()+1)
        if brace<0: continue
        depth=0; end=None
        for i,ch in enumerate(combined[brace:], brace):
            if ch=="{": depth+=1
            elif ch=="}":
                depth-=1
                if depth==0: end=i+1; break
        if end:
            try:
                obj=json.loads(combined[brace:end])
                if obj.get("decision") in ("APPROVE","REQUEST_CHANGES"):
                    decision_obj=obj; break
            except Exception: continue

success=(exit_code==0) and (decision_obj is not None) and (not timed_out)
if decision_obj is not None and "linkage_plan_session" not in decision_obj:
    decision_obj["linkage_plan_session"]=PLAN_SESSION
meta={
  "status":"REVIEW_SUCCESS" if success else "REVIEW_FAILED",
  "timed_out": timed_out,
  "cli_exit_code": exit_code,
  "wall_seconds": wall,
  "prompt_bytes": prompt_bytes,
  "new_session_id": new_session_id,
  "model_route": MODEL,
  "decision": (decision_obj or {}).get("decision"),
  "findings": (decision_obj or {}).get("findings"),
  "reason": (decision_obj or {}).get("reason"),
  "linkage_plan_session": (decision_obj or {}).get("linkage_plan_session", PLAN_SESSION),
  "run_dir": str(run_dir),
  "task_id": TASK_ID,
  "review_commit": REVIEW_COMMIT,
}
(run_dir/"exec-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
payload=decision_obj if decision_obj else {"task_id":TASK_ID,"review_commit":REVIEW_COMMIT,"decision":None,"findings":[],"reason":"parse_failed_or_timeout","linkage_plan_session":PLAN_SESSION,"meta":meta}
(PROJ/"review.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
(PROJ/"stages"/"review").mkdir(parents=True, exist_ok=True)
(PROJ/"stages"/"review"/"review.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
(PROJ/"stages"/"review"/"exec-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(meta, ensure_ascii=False))
raise SystemExit(0 if success else 1)
