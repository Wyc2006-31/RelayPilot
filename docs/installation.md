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
