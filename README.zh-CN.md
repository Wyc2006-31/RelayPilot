# RelayPilot Generation 1

[English](README.md) · [简体中文](README.zh-CN.md)

## 1. 项目介绍

RelayPilot Generation 1 是多 AI 编程接力的实验性工作流：Grok Bot 调度，Codex 规划和审查，云端 WorkBuddy 编程并测试，Magpie 路由本机 Codex 请求，GitHub 负责跨环境代码交接。当前候选为 **v0.1.0-alpha.1 — Preview / Experimental**，公开与 GitHub Release 均等待所有者最终批准。

## 2. 工作流架构

```text
Grok Bot (Webhook / Routine / orchestration)
   -> Codex planning (Windows, existing Magpie route)
   -> WorkBuddy coding + tests (cloud sandbox)
   -> GitHub branch + exact commit + Draft PR
   -> Windows checkout verification + Codex review
   -> bounded rework / next authorized task / stop
```
Windows 本机、Grok Bot 云电脑、WorkBuddy 云端沙箱与 GitHub 不共享文件系统。使用精确 Git Commit 或核验后的导出交接，同名文件不代表已经同步。

## 3. 候选实际包含的功能

保留温度转换模块、包含可选 `--to` 的 CLI 和 35 项原测试；提供可配置的历史静态审查启动器、离线配置校验测试、中英文手动操作指南与不可执行的参考模板。本机示例只使用 Python 标准库。不包含平台 API、Webhook 服务端或已经安装的 Routine。

## 4. Gen 1 完成情况

**本机 VERIFIED：**精确 MINI 快照与温度示例行为。**历史记录 HISTORICAL_RECORD：**本机审查 JSON 记录 MINI-001 至 MINI-004 为 APPROVE；状态与报告记录一次触发依次执行 MINI-003、MINI-004。当前 PR 元数据确认四个未合并 Draft PR，MINI-004 的基线为 MINI-003。**本轮 UNVERIFIED：**全新云端接力、精确 Routine 导出、WorkBuddy 实际服务模型与无人值守恢复。GitHub 交付标识为 cursoragent，历史 WorkBuddy 编程记录需单独理解。

## 5. 安装前提

本机示例需要 Python 3.11+ 和 UTF-8 环境，本次使用 Windows / Python 3.11.9。其他系统与 Python 版本需 CI 或自行验证。完整接力还需要分别安装并登录 Grok Bot、WorkBuddy、Codex CLI、Magpie、GitHub，拥有所需权限，并人工审核 Routine。本项目没有实现一键安装。

## 6. 快速开始

在仓库根目录运行：
```sh
python -X utf8 -B -m unittest discover -s examples/temperature -v
python -X utf8 examples/temperature/temperature_cli.py --from c --value 100 --to f
python -X utf8 -B -m unittest discover -s tests -v
```
预期为示例 35 项通过、CLI 输出 `212.0`、离线配置检查 3 项通过。设置 `PYTHONIOENCODING=utf-8` 时同时设置 `PYTHONUTF8=1`，使子进程读取编码一致。详见[安装](docs/installation.md)和[示例](examples/temperature/README.md)。

## 7. 工作原理

Codex 制定有明确边界与验收条件的计划，WorkBuddy 按精确基线编程并保留原行为和测试。代码通过 GitHub 交接，本机核验提交并测试后才交 Codex 审查。超时、证据缺失或测试失败阻止推进。REQUEST_CHANGES 进入有限返工；APPROVE 仅是审查决定，不授权合并与发布。详见[工作流](docs/workflow.md)。

## 8. GitHub 代码交接

使用自己的沙箱仓库与新任务分支，记录完整 head/parent SHA、文件哈希和测试结果，向正确的前序分支创建 Draft PR。本机测试前核验远程 head。不合并、不强推、不重置已有检出目录、不公开原测试仓库。操作指南描述交接流程，不自动写入 GitHub。

## 9. 模型选择与限制

WorkBuddy 期望优先级：DeepSeek-V4.1-Flash → GLM-5.3 → Kimi-K3 → GLM-5.3-Flash。这是偏好，不是技术强制白名单，也未实现可靠自动切换。UI 选择不能证明实际服务模型；无法确定则为 **UNVERIFIED**。429 限流为已知问题，保持既有 Magpie 路由。详见[模型策略](docs/model-policy.md)。

## 10. 测试结果与证据

2026-11-04 从本地 Git 精确提交提取到隔离目录，在 UTF-8 模式下复跑：MINI-001 为 11/11，MINI-002 为 11/11 转换模块测试及 CLI 冒烟，MINI-003 为 24/24，MINI-004 为 35/35。公开示例保留 MINI-004 的 Python blob，运行 35 项。各版本有重叠，不可累加为独立覆盖数。新增 3 项离线测试仅验证启动前配置安全，不能证明模型调用或云端接力。详见[证据说明](docs/evidence.md)。

## 11. 常见故障

GBK 解码错误：统一 PYTHONUTF8=1 与 UTF-8 输出。缺少可执行文件或配置：运行 --check。429：保存进度，仅在授权预算内重试。审查超时或解析失败：阻塞并检查私人证据，不能补写 APPROVE。跨平台缺文件：按精确 Git Commit 同步。详见[排障](docs/troubleshooting.md)。

## 12. 安全警告

保持 Defender 开启。不上传真实 .env、Token、Cookie、私钥、原始状态、会话、原始审查日志或未经脱敏的媒体。运行日志可能含提示词、代码和模型输出，应放在发布树外或被忽略的 .relaypilot/ 中。不附带 Magpie 二进制；Private 仓库也不能存放秘密。详见[安全指南](SECURITY.md)。

## 13. Roadmap

**PLANNED Gen 1.1：**验证模型选择、限流、状态、幂等和恢复。**PLANNED Gen 1.2：**改进配置、安装、私人日志和监控。**PLANNED Gen 2：**更多 Agent 与可视化任务管理。以上均非已完成功能，详见[路线图](docs/roadmap.md)。

## 14. 贡献指南

阅读 [CONTRIBUTING](CONTRIBUTING.md)。保留原功能和测试，为变更提供证据，保持中英文一致，提交小范围 PR。不提交账号、凭据、私人平台导出与未脱敏截图。

## 15. 许可证

本仓库自有且有权分发的代码与文档使用 [MIT](LICENSE)。第三方软件和服务遵守其各自条款，本项目不授予其再分发权。详见 [NOTICE](NOTICE) 与[第三方审查](docs/third-party.md)。

## 16. Star 支持

如果项目对你有帮助，公开后欢迎 Star。项目不声称任何用户量、性能、下载量或 Star 数据。这是第一代，后续将依据真实验证持续改进。
