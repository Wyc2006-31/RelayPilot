# Gen 1 Preview: first successful run / 第一次成功运行

**Scope / 范围:** run the included local program and tests. No Grok Bot, Codex, Magpie, WorkBuddy account, API key or cloud task is needed. This does not reproduce an automated cloud relay.
运行仓库自带的本机程序和测试，无需上述平台账号、密钥或云任务；这不等于复现自动云端接力。

## 1. Get the source / 获取源码

Install [Python](https://www.python.org/downloads/) 3.11+; Git is optional for ZIP users. Python 3.11 and 3.13 passed the initial Windows/Ubuntu CI. Open a terminal in the parent folder you chose. These are instructions for a **new developer's machine**, not instructions to replace the maintainer's existing checkout.
安装 Python 3.11+；ZIP 用户不必安装 Git。首轮 Windows/Ubuntu CI 的 3.11 与 3.13 已通过。在自己选定的父目录打开终端，以下用于新开发者，不替换维护者现有工程。

The repository is currently Private. Until public approval, only an explicitly authorized GitHub account can clone/download it. Use GitHub's normal sign-in/credential flow; never embed a token in a clone URL. A 404 before authorization is an access issue, not a Python test failure.
仓库目前为 Private，公开批准前只有获授权账号能克隆/下载。按 GitHub 正常流程登录，不把 Token 放进 URL；未授权时的 404 是访问问题，不是 Python 测试失败。

```sh
git clone https://github.com/Wyc2006-31/RelayPilot.git RelayPilot
cd RelayPilot
```

If that folder already exists, use the existing checkout or choose another empty destination; do not overwrite it. Alternatively, on GitHub use **Code → Download ZIP**, extract it, and open the extracted directory containing `README.md`, `scripts/` and `examples/`. For ZIP, skip the clone/cd block. Do not run from `docs/` or `examples/temperature/`.
目录已存在则使用现有检出或另选空目标，不覆盖。也可 Code → Download ZIP，解压后进入同时含 README、scripts、examples 的目录，并跳过克隆步骤。不要在 docs 或示例子目录运行后面的根目录命令。

## 2. Check Python / 检查 Python

```sh
python --version
python -c "from pathlib import Path; print(Path('examples/temperature/temperature_cli.py').is_file())"
```

Expect Python 3.11 or newer and `True`. On Windows, if `python` is unavailable but `py -3` works, replace **each** `python` in this tutorial with `py -3`. On Linux/macOS the command may be `python3`; replace consistently. A wrong working directory prints `False`; return to the repository root. No `pip install`, `.env`, activation script or model login is required.
预期版本 3.11+、第二条为 True。Windows 可统一改用 py -3；Linux/macOS 可统一改用 python3。False 说明工作目录错误，返回仓库根目录。无需 pip、.env、虚拟环境激活或模型登录。

## 3. Run a real conversion / 运行真实换算

```sh
python -X utf8 -B examples/temperature/temperature_cli.py --from c --value 100
python -X utf8 -B examples/temperature/temperature_cli.py --from f --value 32 --to c
python -X utf8 -B examples/temperature/temperature_cli.py --from c --value -40 --to f
```

Expected stdout, respectively: `212.0`, `0.0`, `-40.0`; every command exits 0. `--to` is optional; same-unit conversion returns the input. This is the included converter executing locally, not fabricated relay output.
依次输出 212.0、0.0、-40.0，均 exit 0。--to 可省略，同单位返回输入值。这是真实本机程序输出，不是云接力模拟结果。

## 4. Accept the local example / 验收本机示例

```sh
python -X utf8 -B -m unittest discover -s examples/temperature -v
python -X utf8 -B -m unittest discover -s tests -v
```

Expected: `Ran 35 tests ... OK`, then `Ran 3 tests ... OK`. The latter tests configuration safety without invoking Codex or a model; they create temporary files only under ignored `.build/`. The original test cases are retained. See [encoding troubleshooting](troubleshooting.md) if a shell forces a conflicting output encoding.
预期为 35 项 OK 和 3 项 OK。后三项只验证配置安全，不调用 Codex/模型，仅在被忽略的 .build/ 产生临时文件。原测试完整保留；编码冲突见排障文档。

## 5. Verify a failure / 验证失败路径

Run separately; this command is **expected to fail**:
单独运行以下命令，失败是预期结果：

```sh
python -X utf8 -B examples/temperature/temperature_cli.py --from c --value 100 --to k
```

Expected: no successful conversion on stdout, `invalid choice` on stderr, exit **2**. Immediately inspect `$LASTEXITCODE` in PowerShell, or `echo $?` in a POSIX shell. Do not include this expected nonzero exit in an all-success shell chain.
预期无成功换算输出，stderr 含 invalid choice，退出码 2。PowerShell 紧接着查看 $LASTEXITCODE，POSIX 查看 echo $?。不要把此命令放进要求全部成功的命令链。

## 6. Where to go next / 下一步

Your first reproduction is complete after steps 3–5. For an optional offline launcher configuration check, use [configuration](configuration.md#copyable-offline-check--可复制的离线检查). To understand a human-operated extension, use [manual relay](manual-relay.md). Only consider a new cloud experiment after reviewing accounts, permissions, data scope and cost. Do not replay the maintainer's MINI-003/004 or reuse private Routines, state, credentials or model routes.
完成 3–5 即完成最小复现。可选离线启动器配置检查见配置文档，人工扩展见接力指南。新云实验前自行核对账号、权限、数据范围与费用，不复跑维护者原 MINI-003/004，不复用其私人 Routine、状态、凭据或路由。
