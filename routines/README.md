# Routine integration reference / Routine 集成参考

This is a manual checklist, not an exported Routine, installer or invented API.
这是人工核对表，不是 Routine 导出、安装器或虚构 API。

In Grok Bot UI inspect the existing Webhook trigger, action, task/workflow IDs, execution permissions, result-return handler and continuation/stop rule. Historical records use action `mini_chain` for a bounded two-task run; this repository does not register that action. Keep the working original intact. A new operator must configure their own isolated test Routine via the platform UI, with their own secret kept outside Git. Exact UI labels and export format have not been independently reproduced here.

在 Grok Bot UI 检查既有 Webhook 触发、action、任务/工作流 ID、执行权限、结果回传、继续/停止规则。历史记录使用 mini_chain 执行有限两任务，本仓库不注册该动作。保留正式 Routine。新操作者需通过平台 UI 配置自己的隔离测试 Routine，秘密不入 Git。本次未独立复现精确 UI 标签和导出格式。

Task envelope must name scope, baseline SHA, output branch, tests, maximum tasks/rework, and stop conditions. Require real evidence at every handoff. Cloud sandbox and Windows paths differ. If no reliable result-return/resume path is available, mark BLOCKED and retain evidence. Do not reset original state, duplicate a live trigger or claim an imported Routine exists.

任务应明确范围、基线 SHA、输出分支、测试、最大任务/返工次数和停止条件。每次交接保留真实证据，云端路径与 Windows 不同。无可靠回传/恢复路径则阻塞并保存证据，不重置正式状态、不复制运行中触发器、不声称已导入 Routine。

For a new developer, use [manual relay step 7](../docs/manual-relay.md#7-optional-grok-routinewebhook--可选-grok-调度) to identify the missing platform contract and take the manual path if it cannot be configured. There is no `import`, `register-webhook`, callback server or Routine-creation command in this repository. The JSON configuration example is not an exported Routine. Do not substitute an unrelated Grok/xAI API, WorkBuddy schedule or UI automation for evidence of this original trigger.
新开发者按人工接力第 7 步识别缺失协议，不能配置则走人工路径。仓库没有导入、注册 Webhook、回调服务或创建 Routine 命令；JSON 样例不是 Routine 导出，不以无关 Grok/xAI API、WorkBuddy 定时任务或 UI 自动化冒充原触发证据。
