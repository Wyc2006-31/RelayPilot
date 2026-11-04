# Third-party audit / 第三方审查

Reviewed 2026-11-04. External tools are independently obtained; no application source, binaries, authentication data or model weights are bundled.
于 2026-11-04 核对。外部工具独立获取，不附带应用源码、二进制、认证数据与模型权重。

| Component | Treatment / 处理 | Primary source / 一手来源 |
|---|---|---|
| Codex CLI | External Apache-2.0 project; not vendored / 外部 Apache-2.0 项目，不捆绑 | [upstream license](https://github.com/openai/codex/blob/main/LICENSE) |
| Magpie upstream | MIT upstream; installed binary provenance not established here; no redistribution / 上游 MIT，本机二进制来源未在本次证明，不分发 | [upstream license](https://github.com/yetone/magpie/blob/main/LICENSE) |
| WorkBuddy | External service/software governed by terms; outputs require source review / 外部专有服务与软件，输出仍需来源审查 | [service terms](https://www.workbuddy.cn/document/term) |
| Grok Bot | Installed application identity/distribution rights not established; configuration guidance only / 安装应用身份与再分发权未确证，只写配置指导 | no application files included / 不含应用文件 |
| GitHub | External hosting service; not redistributed / 外部托管服务，不分发 | [terms](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) |
| Python stdlib | Runtime dependency; not bundled / 运行依赖，不打包 | [Python license](https://docs.python.org/3/license.html) |

The owner explicitly authorized extraction of their project material. Small conversion/test files and the owner's orchestration wrapper contain no observed third-party attribution or vendored dependency. This is a source review, not a guarantee that all AI-generated output is copyrightable or unique. MIT applies only to rights contributors can grant. WorkBuddy terms distinguish output ownership from responsibility for third-party rights. Unclear application internals, exports and executable rights are excluded, rather than relicensed.

所有者明确授权提取其项目材料。小型转换/测试文件与自有包装脚本未见第三方署名或捆绑依赖。这是来源审查，不保证 AI 输出均可受版权保护或唯一。MIT 仅适用于贡献者有权授予的部分。WorkBuddy 条款将输出所有权与第三方权利责任区分。权属不明的应用内部文件、导出和可执行程序均排除，不重新授权。
