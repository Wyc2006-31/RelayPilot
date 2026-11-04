# Configuration / 配置

`.env.example` is a reference; the launcher does not load dotenv. Set the `RELAYPILOT_` variables in the shell. Use only your existing Magpie provider definition (`model_provider="magpie"`); no global Codex/Magpie file is changed by the launcher. Do not paste keys into review inputs.

`.env.example` 仅作参考，启动器不加载 dotenv。需在 shell 设置 RELAYPILOT_ 变量，使用已有 magpie provider；脚本不修改全局 Codex/Magpie 配置，不向审查输入粘贴密钥。

Required: CODEX_EXE (executable/path), WORK_DIR (private writable directory), REPO_DIR (separate review checkout), MODEL (existing route), TASK_ID (letters/digits/_/-), REVIEW_COMMIT (40 hex SHA), PLAN_SESSION. Prefix every name with `RELAYPILOT_`. Optional TIMEOUT is 1–120 seconds, default 120. Put the verified, sanitized diff, baseline, tests and acceptance criteria into WORK_DIR/review-input.txt. Manually verify checkout HEAD and review JSON task/SHA; the legacy parser does not enforce this linkage.

必填变量：Codex 可执行文件、私人工作目录、独立审查检出目录、既有模型路由、任务 ID、40 位提交 SHA、计划会话 ID，均以 RELAYPILOT_ 为前缀。TIMEOUT 可选 1–120 秒，默认 120。将核验并脱敏后的 diff、基线、测试和验收写入工作目录的 review-input.txt。必须人工核验检出 HEAD 和审查 JSON 的任务/SHA，历史解析器不强制校验关联。

```sh
python scripts/codex_review.py --check
# Only after approving a real potentially paid call / 仅在同意真实可能付费调用后：
python scripts/codex_review.py --execute
```
Use a fresh empty WORK_DIR for every attempt: the legacy launcher does not enforce immutable attempt directories. Keep it under ignored `.relaypilot/` or outside the publication checkout. Never reuse the live workflow's state directory.
每次使用新的空工作目录，历史启动器不强制不可变尝试目录。放在忽略的 .relaypilot/ 或发布树外，不复用正式工作流状态目录。

WEBHOOK_*, GITHUB_TOKEN and MAGPIE_BASE_URL are platform reference placeholders, not launcher inputs. config/workflow.example.json is documentation, not a supported import API.
平台占位变量不由启动器消费，workflow.example.json 为说明材料，并非可导入 API。
