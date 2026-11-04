# RelayPilot Gen 1

[English](README.md) · [简体中文](README.zh-CN.md)

**Open-source multi-agent AI coding workflow · First-generation Experimental Preview**

Learn how planning, cloud implementation, GitHub handoffs and independent review fit together. Start with a small local example, then explore the documented manual relay. Gen 1 is the first version, with further improvements, refinements and workflow updates planned for future releases.

**Start here:** [first-run local tutorial](docs/preview-quickstart.md) → [optional manual relay](docs/manual-relay.md). The reproducible Gen 1 Preview covers the local example and offline preflight. Full end-to-end automated cloud deployment remains **UNVERIFIED**; these are separate acceptance decisions. See the [Preview scope and release notes](docs/release-notes-v0.1.0-alpha.1.md).

## 1. Introduction

RelayPilot Generation 1 is an experimental multi-AI coding relay: Grok Bot schedules, Codex plans and reviews, cloud WorkBuddy codes and tests, Magpie routes local Codex requests, and GitHub carries code between environments. This first-generation version is **v0.1.0-alpha.1 — Experimental Preview**. The public package focuses on architecture, process, examples, manual handoffs, review and project organization. It is a learning/reference workflow, not a complete commercial automation product; stable unattended end-to-end cloud operation is not promised.

### Why RelayPilot?

Moving a coding task between AI tools creates practical questions: which files are current, which commit was tested, what evidence supports completion, and who reviews the result? RelayPilot documents explicit handoffs using task scope, exact commits, test output and review decisions. Gen 1 lets you study that process and reproduce the local deliverable before configuring your own platform integrations.

## 2. Architecture

```text
Grok Bot (Webhook / Routine / orchestration)
   -> Codex planning (Windows, existing Magpie route)
   -> WorkBuddy coding + tests (cloud sandbox)
   -> GitHub branch + exact commit + Draft PR
   -> Windows checkout verification + Codex review
   -> bounded rework / next authorized task / stop
```
Windows, Grok Bot cloud, WorkBuddy sandbox and GitHub have separate filesystems. Git commits or verified exports are the handoff; equal filenames do not prove synchronization.

## 3. Included in Gen 1

A preserved temperature conversion module, CLI (including optional `--to`) and 35 original tests; a configurable historical static-review launcher; offline launcher preflight tests; bilingual manual runbooks and non-executable reference templates. The local demo uses only Python standard-library modules. There is no bundled platform API, Webhook server or installed Routine.

## 4. Gen 1 status

**VERIFIED locally:** exact MINI snapshots and temperature behavior. **HISTORICAL_RECORD:** local review JSON says APPROVE for MINI-001–004; local state/report records one trigger continuing MINI-003 then MINI-004. Current PR metadata confirms separate unmerged Draft PRs and the MINI-004 → MINI-003 base relationship. **UNVERIFIED here:** a fresh cloud relay, exact exported Routine, WorkBuddy served model and unattended recovery. GitHub delivery metadata identifies cursoragent; historical WorkBuddy coding is a separate evidence claim.

## 5. Prerequisites

For the local demo: Python 3.11+ and a UTF-8 environment. This preparation was tested with Python 3.11.9 on Windows. Other Python/OS versions require CI or your own validation. The full relay also needs independently installed and authenticated Grok Bot, WorkBuddy, Codex CLI, Magpie and GitHub, suitable platform permissions and a reviewed manual Routine. No one-click installation is provided.

## 6. Quick start

Run from the repository root:
```sh
python -X utf8 -B -m unittest discover -s examples/temperature -v
python -X utf8 examples/temperature/temperature_cli.py --from c --value 100 --to f
python -X utf8 -B -m unittest discover -s tests -v
```
Expected: 35 example tests pass, CLI prints `212.0`, and 3 offline preflight tests pass. When setting `PYTHONIOENCODING=utf-8`, also set `PYTHONUTF8=1` so child-process decoding agrees. See [installation](docs/installation.md) and [demo](examples/temperature/README.md).

### Project structure

```text
examples/temperature/  Local converter, CLI and 35 original tests
scripts/              Configurable historical Codex review launcher
tests/                Three offline launcher preflight tests
config/               Documentation-only workflow reference
routines/             Manual Routine/Webhook integration checklist
docs/                 Setup, first run, manual relay, evidence and limitations
.github/              Offline CI and issue templates
```

Start with `docs/preview-quickstart.md`. Runtime credentials, raw sessions, state and local release audits are excluded from the public files.

## 7. How it works

Use Codex to define a bounded task and acceptance criteria. Give the plan and exact baseline to WorkBuddy; retain all existing behavior and tests. Deliver code through GitHub, verify the exact commit locally, then review only the verified input. A review timeout, missing evidence or failed test blocks advancement. `REQUEST_CHANGES` requires bounded rework; `APPROVE` is a review result, never permission to merge or publish. See [workflow](docs/workflow.md).

## 8. GitHub handoff

Use your own sandbox repository and a new task branch. Record full head/parent SHA, file hashes and test results, then open a Draft PR against the intended predecessor. Verify the remote head before local testing. Never merge, force-push, reset an existing checkout or expose the original test repository as part of this demo. The supplied runbooks describe the process; they do not automate GitHub writes.

## 9. Model policy

Desired WorkBuddy priority: DeepSeek-V4.1-Flash → GLM-5.3 → Kimi-K3 → GLM-5.3-Flash. This is a preference, not an enforced whitelist or implemented automatic failover. UI selection is not proof of the served model. Unknown model identity is **UNVERIFIED**. HTTP 429/rate limiting is a known issue. Preserve existing Magpie routing. See [model policy](docs/model-policy.md).

## 10. Tests and evidence

On 2026-11-04, exact local Git snapshots ran in isolated directories: MINI-001 11/11, MINI-002 11/11 converter tests plus CLI smoke, MINI-003 24/24, MINI-004 35/35, with UTF-8 mode enabled. The public example preserves the MINI-004 Python blobs and runs 35 tests. These counts overlap across versions and must not be added as unique coverage. Three new offline preflight tests establish configuration safety only. They do not prove a model call or cloud relay. See [evidence](docs/evidence.md).

## 11. Troubleshooting

GBK decoding errors: align `PYTHONUTF8=1` and UTF-8 subprocess output. Missing executable/config: run the launcher with `--check`. 429: stop and save progress; retry only within an approved budget. Review timeout or parser failure: block, inspect private evidence, never synthesize APPROVE. Files missing across platforms: synchronize through the exact Git commit. See [troubleshooting](docs/troubleshooting.md).

## 12. Security

Keep Defender enabled. Never upload real `.env`, tokens, cookies, private keys, raw state, sessions, raw review logs or unsanitized media. Runtime logs can contain prompt/code/model output; keep work directories outside the publication tree or in ignored `.relaypilot/`. No Magpie executable is bundled. Private repository visibility does not make secrets safe. See [SECURITY](SECURITY.md).

## 13. Roadmap

**PLANNED Gen 1.1:** verify model selection, rate-limit behavior, state/idempotency and recovery. **PLANNED Gen 1.2:** improve configuration, installation, private logging and monitoring. **PLANNED Gen 2:** additional agents and visual task management. These are not implemented capabilities. See [roadmap](docs/roadmap.md).

## 14. Contributing

Read [CONTRIBUTING](CONTRIBUTING.md). Preserve original behavior and tests, provide evidence for changes, keep English and Chinese docs aligned, and submit small PRs. Never include accounts, credentials, private platform exports or unsanitized screenshots.

## 15. License

Repository-owned distributable code and documentation: [MIT](LICENSE). External services and software keep their own licenses and terms; nothing here grants rights to redistribute them. See [NOTICE](NOTICE) and [third-party review](docs/third-party.md).

## 16. Support

If this workflow helps you learn or build, consider giving RelayPilot a Star and sharing a reproducible improvement or issue. There are no claimed user, performance, download or Star statistics. This is the first generation, not the final form; future versions will continue to refine and update the workflow with evidence.
