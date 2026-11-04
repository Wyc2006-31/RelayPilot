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

## Copyable offline check / 可复制的离线检查

Open a **new PowerShell session** in a Git clone's root after installing Codex CLI. This block creates a unique ignored work directory. It leaves the existing provider configuration untouched and never calls the model. ZIP users can finish the local tutorial without this optional Git-based check.
安装 Codex CLI 后在 Git 克隆根目录打开新的 PowerShell 窗口。本段创建唯一的被忽略工作目录，不改已有 provider 配置、不调用模型。ZIP 用户可完成本机教程，无需这项可选 Git 检查。

```powershell
$repoRoot = (Get-Location).Path
if (-not (Test-Path -LiteralPath 'scripts/codex_review.py')) { throw 'Open the repository root first' }
$sha = (git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $sha -notmatch '^[0-9a-fA-F]{40}$') { throw 'Use a Git clone with a real commit' }
$attempt = Join-Path $repoRoot ('.relaypilot/preflight-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $attempt -ErrorAction Stop | Out-Null
Set-Content -LiteralPath (Join-Path $attempt 'review-input.txt') -Encoding utf8 -Value 'OFFLINE CONFIGURATION CHECK ONLY. Not review evidence.'
$env:RELAYPILOT_CODEX_EXE = (Get-Command codex -ErrorAction Stop).Source
$env:RELAYPILOT_WORK_DIR = $attempt
$env:RELAYPILOT_REPO_DIR = $repoRoot
$env:RELAYPILOT_MODEL = 'CONFIG_CHECK_ONLY'
$env:RELAYPILOT_TASK_ID = 'PREVIEW-CHECK-001'
$env:RELAYPILOT_REVIEW_COMMIT = $sha
$env:RELAYPILOT_PLAN_SESSION = 'OFFLINE_CONFIG_CHECK'
$env:RELAYPILOT_TIMEOUT = '120'
python -X utf8 -B scripts/codex_review.py --check
if ($LASTEXITCODE -ne 0) { throw 'Preflight failed; inspect the configuration error' }
```

Expected stdout: `CONFIG_VALID; model execution NOT performed; served_model=UNVERIFIED`. The fake model/plan labels above are deliberately offline configuration values, not a claimed model or real planning session. **Do not append --execute to this setup.** Successful preflight does not inspect Codex provider definitions, authenticate, check out the SHA, test input truth or establish network reachability.
预期输出如上，示例模型/计划标签仅用于离线配置，不代表真实服务或规划会话。不要在此配置后直接改成 --execute。预检通过不代表核对过 provider、认证、SHA 检出、输入真实性或网络。

## Isolated provider reference / 隔离提供商参考

This is a **manual, unexecuted network-configuration reference** for a new operator using a default loopback Magpie gateway. It is not loaded by `.env.example`, and it is not a project-local `.codex/config.toml`. Open a separate shell, choose a fresh ignored directory such as `.relaypilot/codex-preview-UNIQUE`, create it, and set `CODEX_HOME` in that shell to its absolute path. Then manually create `config.toml` inside that new directory with the following provider definition. Never overwrite an existing file or copy auth/state from a working profile.
以下是新操作者默认回环 Magpie 网关的人工网络配置参考，未在本轮执行联网验证；.env.example 不会加载它，也不是项目级 .codex/config.toml。在另一个新 shell 新建唯一的忽略目录，将该 shell 的 CODEX_HOME 设为其绝对路径，再在其中人工创建 config.toml。不要覆盖已有文件，也不要复制正式 profile 的认证/状态。

```toml
[model_providers.magpie]
name = "Magpie local preview"
base_url = "http://127.0.0.1:3425/v1"
wire_api = "responses"
env_key = "RELAYPILOT_GATEWAY_KEY"
requires_openai_auth = false
```

`CODEX_HOME` selects Codex's user-state directory, and provider definitions belong at that user level. The provider ID must remain `magpie` because the launcher selects it explicitly. See [official Codex configuration](https://learn.chatgpt.com/docs/config-file/config-reference) and [state location](https://learn.chatgpt.com/docs/config-file/config-advanced).
CODEX_HOME 选择用户状态目录，provider 定义放在该用户级配置内；启动器固定选择 magpie，因此 ID 应一致。字段与目录依据官方 Codex 文档。

For the documented local-loopback default only, set `RELAYPILOT_GATEWAY_KEY` in that same shell to `magpie-relaypilot`, an application-identification value accepted by that default gateway, **not a vendor API secret**. If your gateway requires a real key, use your own secure local credential process instead; this loopback example is not a remote-gateway authentication recipe. Adjust the loopback port to your own installation when necessary. Add the actual provider account/key **inside your own Magpie**, and select an available route there. See [Magpie gateway documentation](https://usemagpie.ai/docs/integrate). Do not export a local loopback URL to a cloud task expecting it to reach your PC.
仅对官方文档所述默认本机回环情况，在同 shell 将 RELAYPILOT_GATEWAY_KEY 设为应用标识 magpie-relaypilot，不是厂商密钥。如网关要求真实 Key，应按自己的安全凭据流程处理，本例不用于远程认证。端口按自己安装调整，厂商账号/Key 在自己的 Magpie 内添加并选实际路由。云任务的回环地址不会连接到你的 PC。

Before a separately authorized real review, use a **different new work directory**, real sanitized review input, real planning-session ID and verified delivery SHA. Replace `RELAYPILOT_MODEL` with the route from your own Magpie. Confirm checkout HEAD yourself; the launcher does not do that. Only then deliberately use `--execute`. Close the isolated shell afterwards to discard its environment settings; do not write these to global shell profiles. No live provider/model/cloud test was performed by this documentation update.
单独批准真实审查后，另用全新工作目录、真实脱敏输入、真实计划关联和核验后的提交 SHA，将模型改为自己的实际路由；人工确认 HEAD 后才主动 --execute。关闭隔离 shell 即结束环境设置，不写全局 profile。本轮文档更新未验证真实 provider、模型或云任务。
