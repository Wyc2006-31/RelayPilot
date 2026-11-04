# Manual relay setup / 人工接力搭建

**This is an operator runbook, not an automatic deployment script.** Steps below describe a new developer's isolated sandbox. No step authorizes changing the maintainer's running system. Local Preview acceptance is [independent](preview-quickstart.md) of these optional platform integrations.
这是人工操作指南，不是自动部署脚本。仅针对新开发者自己的隔离沙箱，不授权修改维护者正式系统；本机预览验收不依赖这些可选集成。

## Included, self-configured, unavailable / 三类边界

| Component / 组件 | Included executable / 仓库可执行内容 | Operator setup / 自行配置 | Unavailable or unverified / 未提供或未验证 |
|---|---|---|---|
| Python demo | converter, CLI, 35 tests / 转换、CLI、35 测试 | Python / Python 环境 | no cloud scheduler / 无云调度 |
| Codex | review launcher + 3 offline tests / 审查启动器与 3 项预检 | install CLI, provider, real review input / 安装、提供商、真实审查输入 | real call not replayed this round / 本轮未真实调用 |
| Magpie | no executable/config bundled / 不附程序或真实配置 | provider login/key, route, loopback gateway / 登录或密钥、路由、本机网关 | served model / 实际模型未证明 |
| WorkBuddy | no cloud executor/API client bundled / 不附云执行器或 API 客户端 | own login, workspace, repo permission, task / 自己登录、空间、仓库授权、任务 | original private task export / 原私人任务未导出 |
| GitHub | written handoff procedure / 交接说明 | own sandbox repo, branch, authentication / 自建沙箱仓库、分支、认证 | no automatic PR/merge provisioner / 无自动 PR/合并部署器 |
| Grok Routine/Webhook | reference checklist only / 仅参考核对表 | correct app/account entitlement and own supported trigger / 正确应用、账号权限、支持的触发器 | exact original export/callback contract unavailable / 原导出和回传协议未取得 |

## 1. Separate sandbox and identities / 隔离沙箱与身份

First pass the local tutorial. Choose a **different repository you own** for experiments; do not grant a cloud executor write access to this release candidate or the maintainer's test repo. In GitHub, manually create that sandbox as Private, initialize a README, and write down its HTTPS clone URL, default branch and repository owner. Authorize Git through the platform's normal login; grant only this sandbox when repository selection is offered. No PAT values belong in prompts, Git remotes or examples.
先通过本机教程。实验使用自己另一个仓库，不给云执行器本候选库或维护者测试库的写权限。在 GitHub 人工创建 Private 沙箱并初始化 README，记录 HTTPS URL、默认分支和所有者。正常登录 Git；可选仓库授权时仅选该沙箱，不把 PAT 值放进提示词、remote 或示例。

In a new empty destination, clone your sandbox. Replace the **whole quoted value** below with your own URL first:
在新空目标克隆自己的沙箱，先替换下方整个引号中的 URL：

```powershell
$sandboxUrl = 'https://github.com/YOUR_OWNER/YOUR_SANDBOX.git'
git clone $sandboxUrl relay-sandbox
if ($LASTEXITCODE -ne 0) { throw 'Clone failed; check access before continuing' }
Set-Location relay-sandbox
$baseline = (git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0) { throw 'No baseline commit' }
git status --short
```

Expect a 40-character baseline SHA and no uncommitted changes. Choose a unique output branch such as `preview-docs-001`. Give the executor that baseline and output branch; do not ask it to modify a shared branch. These are manual commands, not something RelayPilot runs for you.
预期得到 40 位基线 SHA 且工作区干净。选唯一输出分支，把基线和分支交给执行者，不要求修改共享分支。以上是人工命令，不是 RelayPilot 自动执行。

## 2. Codex and Magpie / Codex 与 Magpie

Install Codex CLI independently and check `codex --version` and `codex exec --help`. Open Magpie on **your own machine**, add your own provider under Providers and complete its sign-in/key entry in the application. Record an actually available model/route. Agent wiring can modify that user's agent configuration, so use an isolated setup rather than copying the maintainer's files. See [Magpie getting started](https://usemagpie.ai/docs/start).
独立安装 Codex 并运行版本/help 检查。在自己的机器打开 Magpie，于 Providers 添加自己的提供商并在应用内完成登录/密钥输入，记录实际可用路由。Agent 连接会改该用户的 Agent 配置，因此使用隔离环境，不复制维护者文件。参见官方入门。

The bundled launcher explicitly requests provider ID `magpie`. Selecting a model in a current UI does not itself prove that this named provider exists. Use the isolated configuration recipe in [configuration](configuration.md#isolated-provider-reference--隔离提供商参考), or have your own operator verify an existing compatible named provider. `--check` verifies fields/files/executable only; it proves neither network/authentication nor model availability. No OpenAI login is required for the local demo; real authentication depends on the provider you chose.
启动器明确使用 magpie provider ID，UI 选模型不证明这个同名 provider 已存在。可按隔离配置配方设置，或由操作者核对自己的兼容配置。--check 仅查字段/文件/程序，不证明网络、认证或模型可用。本机示例不需要 OpenAI 登录；真实认证取决于自选提供商。

## 3. Plan and hand off to WorkBuddy / 规划后交给 WorkBuddy

After separately approving any real model use, ask Codex for a bounded plan. A first **new** sandbox task can be documentation-only, e.g. add a short usage paragraph to the sandbox README without touching code/tests. The following is a human-readable task brief to fill in, **not an API payload**:
单独批准真实模型使用后，让 Codex 给出有限计划。首次新沙箱任务可只给 README 加一小段用法，不改代码测试。以下是需填写的人读任务书，不是 API 请求：

```text
Task: PREVIEW-DOCS-001
Repository: YOUR_OWNER/YOUR_SANDBOX
Baseline: YOUR_FULL_BASELINE_SHA
Output branch: YOUR_UNIQUE_TASK_BRANCH
Allowed change: one README usage paragraph; retain all existing content
Acceptance: review diff; run existing repository tests if present
Delivery: full commit SHA, parent SHA, changed files, test command + exit
Stop: after delivery; no merge/release/next task; at most one requested repair
```

Sign into your own WorkBuddy. Create a **new** task and choose its workspace before sending the plan. For a local Git workspace, current official docs describe a branch selector; a cloud workspace must receive repository access or a sanitized source export separately. Follow your installed version's authorization screens; if no GitHub/cloud integration is exposed, use the export handoff below instead of inventing an endpoint. See [task creation](https://www.workbuddy.cn/docs/workbuddy/Create-Task) and [Git workspaces](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Worktree-Task).
登录自己的 WorkBuddy，新建任务并先选工作空间。官方文档对本机 Git 工作空间描述了分支选择器；云空间另需仓库权限或脱敏源码导出。按安装版本的授权页操作；无 GitHub/云集成入口时走下述导出交接，不虚构接口。参见官方建任务和 Git 空间文档。

Record the workspace environment and visible model label; do not put a Windows path into a cloud task as if it were mounted. WorkBuddy's scheduled-cloud feature is not the original Grok Webhook relay and is not required here. A custom local WorkBuddy model setting is not proof of the cloud executor's model. If served-model evidence is absent, record `UNVERIFIED`.
记录空间环境与 UI 模型标签，不把 Windows 路径当成云端挂载。WorkBuddy 云定时任务不等同于原 Grok Webhook 接力，本指南不要求创建它。本机自定义模型设置不能证明云执行模型；无 served 证据则写 UNVERIFIED。

## 4. Deliver through GitHub / 通过 GitHub 交接

If the cloud environment has authorized sandbox access, have it deliver only the agreed branch and return the full SHA. Open the Draft PR in GitHub's normal compare workflow: check base repository/branch and compare branch, use **Create draft pull request**, and verify the displayed head SHA. Do not press merge. If an additional delivery agent pushes files, record its identity separately from the coding agent.
云环境有沙箱权限时，仅交付约定分支并回传完整 SHA。在 GitHub compare 流程核对 base 仓库/分支与 compare 分支，创建 Draft PR 并核验 head SHA，不合并。另有 Agent 推送时单独记录交付身份。

If direct push is unavailable, export **only the agreed changed files** and a file list with SHA256 digests. A human copies them into a new sandbox checkout, checks hashes/content, runs its tests and commits on a new task branch. Use that new commit SHA as delivery evidence. This is a manual export path; it does not establish automated cloud-to-GitHub synchronization. Do not transfer state, sessions or credentials. See [GitHub's Draft PR guide](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
无法直接推送时，仅导出约定变更文件与 SHA256 清单，由人复制到全新沙箱检出、核哈希与内容、跑测试、在新任务分支提交，并以新提交 SHA 作为交付证据。这是人工导出，不证明自动同步，不转移状态、会话和凭据。

## 5. Verify exact delivery locally / 本机核验精确交付

Return to a separate empty destination. Use a full GitHub-reported SHA, not only a branch label. These commands are for your sandbox and must not be run against existing production checkouts:
另选空目标，以 GitHub 返回的完整 SHA 核验，不只看分支名。命令仅针对自己的沙箱，不用于已有正式检出：

```powershell
$sandboxUrl = 'https://github.com/YOUR_OWNER/YOUR_SANDBOX.git'
$delivered = 'YOUR_FULL_40_CHARACTER_DELIVERY_SHA'
$baseline = 'YOUR_FULL_40_CHARACTER_BASELINE_SHA'
if ($delivered -notmatch '^[0-9a-fA-F]{40}$' -or $baseline -notmatch '^[0-9a-fA-F]{40}$') { throw 'Replace SHA placeholders' }
git clone $sandboxUrl relay-review
if ($LASTEXITCODE -ne 0) { throw 'Clone failed' }
Set-Location relay-review
git checkout --detach $delivered
if ($LASTEXITCODE -ne 0) { throw 'Exact commit unavailable; stop' }
if ((git rev-parse HEAD).Trim() -ne $delivered) { throw 'Wrong checkout' }
git merge-base --is-ancestor $baseline $delivered
if ($LASTEXITCODE -ne 0) { throw 'Delivery is not based on the agreed baseline' }
git rev-list --parents -n 1 HEAD
git diff --stat $baseline $delivered
git diff $baseline $delivered -- README.md
```

A task can contain multiple commits, so the immediate parent need not equal the baseline; verify ancestry and inspect every commit/file within scope. Run that sandbox's real documented tests and record exit codes. Do not substitute RelayPilot's 35 converter tests for an unrelated sandbox's tests.
任务可能含多次提交，直接 parent 不必等于基线；需查祖先关系及范围内全部提交/文件。运行该沙箱自身真实测试并记录退出码，不能用 RelayPilot 的 35 项替代无关项目测试。

## 6. Review and stop / 审查并停止

Prepare a sanitized `review-input.txt` containing task ID, exact baseline/delivery SHA, acceptance criteria, changed file diff and actual test command/exit/output. Use a fresh work directory, configure the launcher as documented and obtain approval for `--execute` before making a real call. This launcher reviews supplied text; it does not fetch the PR or rerun tests. Manually compare `task_id`, `review_commit`, `linkage_plan_session`, the raw decision and execution metadata. `REQUEST_CHANGES`, timeout, parse failure or wrong SHA blocks acceptance; launcher exit 0 alone is insufficient. After at most the agreed repair, stop; no automatic next task/merge/release is provided.
脱敏审查输入包含任务 ID、精确基线/交付 SHA、验收、diff 和真实测试记录。使用新工作目录，按配置文档设置，获真实调用授权后才 --execute。启动器只审输入文本，不自动取 PR 或跑测试。人工比对任务、提交、计划关联、决定与执行元数据。REQUEST_CHANGES、超时、解析失败或 SHA 错误均阻止验收，exit 0 不足以放行。至多约定返工后停止，无自动下一任务/合并/发布。

## 7. Optional Grok Routine/Webhook / 可选 Grok 调度

The exact installed Grok Bot distribution, entitlement-specific UI and portable Routine/callback schema have not been established for other developers. Do not substitute xAI chat/API docs for this application's automation interface. Therefore no URL, HTTP method, auth header, payload or import button is prescribed here. A fabricated `curl` trigger would be misleading.
未确证其他开发者所用 Grok Bot 发行版、权限相关 UI 和可移植 Routine/回传 schema。不要用 xAI 聊天/API 文档代替该应用自动化接口。因此不规定 URL、HTTP 方法、认证头、payload 或导入按钮，虚构 curl 触发会误导。

On your own supported account, locate the app's actual automation/Routine feature, **create a separate disabled test item if supported**, and record: app version, trigger contract from that app, permissions, task brief, Windows/cloud execution boundary, result-return channel, unique task/workflow identity, task/retry budget and stop rule. Keep generated URLs/secrets in private platform storage. If any of trigger delivery, result return or continuation cannot be configured through supported controls, mark this integration `UNVERIFIED` and use steps 1–6 manually. Do not create a schedule just to imitate the unavailable Webhook.
在自己受支持账号中找到应用真实自动化入口；支持时仅建独立、禁用的测试项，记录版本、该应用给出的触发协议、权限、任务书、Windows/云边界、结果回传、唯一任务/工作流标识、任务/重试预算与停止规则。生成的 URL/秘密留在私人平台存储。触发、回传或继续任一环节不能由受支持控件配置时，标 UNVERIFIED，人工执行 1–6，不用定时任务冒充 Webhook。

This checklist is the limit of portable instructions currently supported by evidence, not a claim that the full relay can be independently deployed. [Routine reference](../routines/README.md) and [evidence levels](evidence.md) preserve the historical record without requiring a replay of MINI-003/004.
这是当前证据支持的人工指导边界，不代表完整接力可独立部署。参考 Routine 与证据分级保留历史记录，不要求复跑原 MINI-003/004。
