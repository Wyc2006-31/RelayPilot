# Limitations / 能力边界

- No portable exported Grok Routine, cloud provisioner, authenticated Webhook integration test or WorkBuddy API is bundled. Full third-party cloud replay remains UNVERIFIED.
- Historical one-trigger evidence is a local state/report claim corroborated by commits/tests, not a newly observed trigger or proof of reliability.
- A cloud delivery commit may identify a different agent from the recorded coding tool. Do not infer WorkBuddy execution solely from commit metadata.
- No enforced four-model whitelist, automatic failover, served-model attestation, continuous monitor or reliable crash recovery.
- The extracted launcher retains a permissive legacy decision parser, no strict task/SHA/schema gate, no immutable attempts and no log redactor. It can accept a parsed REQUEST_CHANGES as REVIEW_SUCCESS; never automate advancement on exit 0 alone.
- The 120-second timeout kills the direct child; termination of every descendant is not guaranteed. There is no durable process supervisor. Never start another attempt before checking for remaining processes.
- Existing float behavior (including bool inputs and nonfinite values) is preserved; this is a workflow sample, not a scientific validation library. CLI target aliases are the original lowercase choices.
- Only a local Windows/Python 3.11.9 replay was performed during preparation. Third-party subscriptions, UI changes and costs remain the operator's responsibility.

- 不包含可移植 Grok Routine 导出、云环境部署器、已认证 Webhook 集成测试或 WorkBuddy API；完整第三方云端复跑为 UNVERIFIED。
- 单次触发来自历史状态/报告，提交与测试提供旁证，不是本次观察到的触发，也不证明可靠性。
- 交付提交可能显示不同于编程记录的 Agent，不能仅靠 Git 元数据证明 WorkBuddy 编程。
- 没有四模型强制白名单、自动切换、实际模型证明、持续监控与可靠崩溃恢复。
- 启动器保留宽松历史解析器，不强校验任务/SHA/schema、不保证不可变尝试目录、无日志脱敏。解析到 REQUEST_CHANGES 也可为 REVIEW_SUCCESS，不能仅凭 exit 0 推进。
- 120 秒超时只终止直接子进程，不保证所有后代进程终止，也没有持久监督器；确认无残留后才开始下一次。
- 保留 bool、非有限数值等原 float 行为；示例不是科学校验库。目标别名保留原有小写 choices。
- 本次本机复跑仅为 Windows / Python 3.11.9，订阅、UI 变化与费用需操作者自行核验。
