# Architecture / 架构

The scheduler and cloud tools remain external. The publication is a reproducible local example, historical launcher and manual integration reference. There is no new orchestration engine replacing the original workflow.

调度与云工具仍在外部。本候选提供可复现本机示例、历史启动器和人工集成说明，不重写或替换原有工作流。

| Environment / 环境 | Owns / 职责 | Handoff / 交接 |
|---|---|---|
| Grok Bot cloud | Webhook, Routine, task continuation / 调度与继续 | task/plan/evidence references / 任务与证据引用 |
| Windows | Codex plan/review, verification, existing Magpie route / 规划审查与核验 | exact Git commit or verified export / 精确提交或核验导出 |
| WorkBuddy sandbox | implementation, tests, bounded repair / 编程测试返工 | code + test evidence / 代码与测试证据 |
| GitHub | branches, commits, Draft PRs / 版本交接 | immutable SHA; separate from approval / 提交 SHA 与审查分离 |

Historical GitHub delivery metadata includes cursoragent; it is not proof of the coding executor. WorkBuddy and Grok cloud files are not mounted onto Windows by this repository.
历史交付元数据包含 cursoragent，不能凭此证明编程执行者；本仓库不会把两个云端文件系统挂载到 Windows。
