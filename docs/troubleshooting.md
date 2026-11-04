# Troubleshooting / 排障

| Symptom / 现象 | Action / 处理 |
|---|---|
| UnicodeDecodeError / GBK | Set PYTHONUTF8=1 for parent/children; align output encoding. Do not delete failing tests. / 父子进程统一 UTF-8，不删除失败测试。 |
| Missing configuration/executable | --check, shell environment, executable path and input file. / 检查环境变量、程序路径和输入文件。 |
| 429 | Save evidence; bounded retry with user-approved budget; actual model remains unknown without evidence. / 保存证据，按授权预算有限重试，无证据不认定模型。 |
| Review timeout/invalid JSON | Block; inspect private logs and manually validate exact task/SHA. No fabricated approval. / 阻塞，检查私人日志和关联，不补写批准。 |
| Cloud files absent locally | Fetch exact Git commit into a fresh checkout or verify an authorized export hash. / 新检出精确提交或核验授权导出哈希。 |
| Defender alert | Keep protection on; exclude the binary from publication and resolve via trusted channels. / 保持防护，候选排除二进制，走可信渠道处理。 |
| Stale last-message/result | New empty work directory per attempt; do not treat old approval as current. / 每次使用全新空目录，旧批准不代表本次。 |

Report a sanitized command, exit code, tool version and expected behavior. Do not attach raw logs or screenshots containing secrets.
报告脱敏后的命令、退出码、版本和预期，不附带含秘密的原始日志和截图。
