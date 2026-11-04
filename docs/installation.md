# Installation / 安装

1. Obtain this candidate in a new directory; install Python 3.11+ independently.
2. Run the three README commands. No pip dependencies or API keys are needed for this local demo.
3. For a real relay, independently install/authenticate the external tools through their official distribution channels. Preserve existing routes and Routines. This candidate cannot configure your cloud accounts.
4. Follow configuration.md and workflow.md in your own isolated sandbox. Platform steps require UI access and may incur costs; review them before execution.

1. 在独立目录获取候选，单独安装 Python 3.11+。
2. 执行 README 三条命令；本机示例不需要 pip 依赖与 API Key。
3. 完整接力需从各官方渠道分别安装、登录，保留既有路由和 Routine。本仓库不能配置你的云账号。
4. 在自己的隔离沙箱按配置和工作流文档操作，云端步骤需要 UI 权限且可能收费，应先审核再执行。

PowerShell UTF-8 setup / PowerShell 编码设置：
```powershell
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'
python -B -m unittest discover -s examples/temperature -v
```
Linux/macOS commands are provided as portable Python usage but not claimed locally verified. CI checks its own matrix separately.
Linux/macOS 的 Python 命令具备可移植形式，但不声称本机已验证；CI 结果按其实际矩阵单独报告。

## Choose a track / 选择搭建范围

Start at [the step-by-step local tutorial](preview-quickstart.md). It covers source access, the correct working directory, executable selection, real output, both test suites and an expected failure. It works without the maintainer's paths, private data, platform accounts or original state.
先按最小教程逐步操作：源码访问、工作目录、Python 命令、真实输出、两套测试和预期失败，均不依赖维护者路径、私人资料、平台账号或原状态。

| Track / 路径 | Install / 安装 | Sign-in and authorization / 登录与授权 | Acceptance / 验收 |
|---|---|---|---|
| Local Preview / 本机预览 | Python 3.11+; Git optional with ZIP / Python，ZIP 可免 Git | Private source requires explicit repository access until publication / 公开前需仓库访问权 | 35 example + 3 offline tests / 35+3 项 |
| Launcher preflight / 启动器预检 | Python + [Codex CLI](https://github.com/openai/codex) | --check needs no provider login; requires a discoverable executable / 无需模型登录，但需程序可找到 | CONFIG_VALID, no model call / 配置有效，无调用 |
| Manual relay / 人工接力 | above plus own Magpie and WorkBuddy installation / 再自行安装 Magpie、WorkBuddy | own provider authentication, WorkBuddy login, sandbox GitHub access / 自有认证和沙箱权限 | exact SHA, real test evidence, manually checked review / 提交、测试、人工核对审查 |
| Grok automation / Grok 自动接力 | correct Grok Bot distribution + feature entitlement / 正确发行版与功能权限 | own Routine/Webhook and execution authorization / 自配 Routine、触发和执行权限 | UNVERIFIED; no portable original export / 未验证，无原可移植导出 |

Do not install cloud tooling just to run the converter. No service is started by cloning this repository. See [manual relay](manual-relay.md) for the optional human handoffs; lack of Grok automation does not block local Preview acceptance.
仅运行转换示例不必装云工具，克隆不会启动服务。可选人工交接见指南；缺 Grok 自动化不阻止本机预览验收。

Initial CI evidence (2026-11-04): Windows/Ubuntu × Python 3.11/3.13 passed. This is CI evidence, not a claim of a locally tested macOS installation or live cloud integration.
首轮 CI 证据为 Windows/Ubuntu × Python 3.11/3.13 通过，不代表本机验证了 macOS 安装或真实云集成。
