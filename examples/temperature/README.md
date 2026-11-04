# Temperature relay example / 温度接力示例

Purpose: replay the smallest safe result of the historical coding relay locally, without platform credentials. Four original Python files retain the MINI-004 conversion, CLI and tests; no workflow engine is simulated.
用途：无需平台凭据在本机复跑历史接力的最小安全产物。四份 Python 文件保留 MINI-004 算法、CLI 与测试，不模拟工作流引擎。

Environment: Python 3.11.9 on Windows was tested. No third-party package. From a clean repository directory:
环境：本次验证为 Windows / Python 3.11.9，无第三方包。在干净仓库目录运行：

```sh
python -X utf8 -B -m unittest discover -s examples/temperature -v
python -X utf8 examples/temperature/temperature_cli.py --from c --value 100
python -X utf8 examples/temperature/temperature_cli.py --from f --value 32 --to c
python -X utf8 examples/temperature/temperature_cli.py --from c --value 100 --to k
```

Acceptance: 35 tests, exit 0; first CLI prints `212.0`, exit 0; second prints `0.0`, exit 0; final invalid choice exits 2 and writes stderr. Negative values, aliases and same-unit behavior are tested. Invalid value/missing required arguments must fail, not silently succeed. See docs/troubleshooting.md for UTF-8 mode if parent/child encoding differs.
验收：35 项测试且 exit 0；首条 CLI 输出 212.0；第二条输出 0.0；非法目标以 exit 2 和 stderr 结束。测试含负数、别名和同单位。非数字、缺参数必须失败；编码不一致见排障文档。

Optional extension: use routines/README.md and docs/workflow.md to manually request a bounded change through your own Grok/WorkBuddy setup, GitHub sandbox and Codex review. This cloud extension was not freshly executed during preparation and has no exported importable Routine. It can incur charges. Local success does not establish full relay reproducibility.
可选扩展：在自己的 Grok/WorkBuddy 配置、GitHub 沙箱和 Codex 审查中，按指南人工发起有边界的变更。本次没有新执行该云端扩展，也没有可导入 Routine，可能收费；本机通过不能证明完整接力可复现。
