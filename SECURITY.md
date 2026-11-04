# Security / 安全

Never put real credentials or personal data in an issue, PR or committed file. Use GitHub private vulnerability reporting if enabled; otherwise notify the maintainer privately through an already trusted channel without sending the secret itself. Public reports should contain only sanitized category, relative path, severity and remediation status. Rotate affected credentials if exposure is confirmed.

不在 issue、PR 或提交中放真实凭据与个人资料。有 GitHub 私人漏洞报告时使用该渠道，否则通过已有可信私人渠道联系维护者，不发送秘密值。公开报告仅含脱敏类别、相对路径、严重度与处理状态。确认泄露需轮换相应凭据。

Keep Windows Defender enabled, never add an exclusion for this project, and obtain external tools from trusted official channels. No Magpie binary is shipped. Do not copy browser profiles, platform data directories, raw state, personal logs or session databases. The launcher writes raw private evidence; it does not redact model output. Review inputs are sent to the configured provider only with --execute, which can incur costs. Prompt rules are not a complete security boundary.

保持 Defender 开启，不为项目添加排除项，外部工具从官方可信渠道获取。不分发 Magpie 二进制，不复制浏览器资料、平台数据目录、原始状态、个人日志或会话数据库。启动器写原始私人证据，不自动脱敏模型输出。--execute 才向配置提供商发送输入，可能收费；提示词规则不是完整安全边界。

Before publication: inspect a whitelist, scan candidate and history with a dedicated secret scanner plus manual privacy/license review, audit filename/links/binaries, exclude release-audit/. A private repository is not a credential store. Automation uses read-only repository permissions, no private keys, no auto-merge and no release deployment.

公开前按白名单逐文件审核，专用扫描器检查候选与历史，人工复核隐私、许可证、文件名、链接与二进制，排除 release-audit/。Private 仓库不是凭据库。自动化只读权限、不用私人密钥、不自动合并与发布。
