# Workflow / 工作流

1. In the Grok Bot UI inspect your existing Webhook/Routine, permissions, task ID, trigger, result return and stop rules. Do not overwrite an existing Routine. A portable original export is not included; see routines/README.md.
2. Codex plans the authorized scope, file whitelist, exact baseline commit, tests and bounded retries. Preserve original options, text processing and behavior.
3. In the WorkBuddy UI open a separate task, select a desired model and record its UI label separately from served-model evidence. Provide plan and Git baseline. Require actual test output and Git handoff.
4. Deliver a branch and Draft PR; record head and parent SHA, changed files and test command/exit. If a separate delivery agent is used, record it separately from the coding executor.
5. Use a fresh local checkout of the exact SHA; compare hashes and run all original tests. Never hard-reset an existing user's checkout.
6. Give sanitized verified evidence to Codex. Retain review JSON and execution exit/timeout privately. Validate task and commit linkage yourself. REVIEW_SUCCESS means a decision parsed; it may be REQUEST_CHANGES.
7. On REQUEST_CHANGES return specific location, problem, impact, reproduction and acceptance criteria to the same bounded work item. Failed/timeout/unknown blocks advancement; preserve evidence. No indefinite retry.
8. Continue only to the next explicitly authorized task. Historical two-task evidence stopped after MINI-004. Completion does not imply merge, publication, durable pause/resume or 24-hour monitoring.

1. 在 Grok Bot UI 检查既有 Webhook/Routine、权限、任务 ID、触发、结果回传与停止规则。不覆盖既有 Routine。本候选不附带可移植原导出。
2. Codex 规划授权范围、文件白名单、精确基线、测试和有限重试，保留原参数、文本处理与行为。
3. WorkBuddy UI 开独立任务，记录选择标签与实际服务模型证据的差别，提供计划和 Git 基线，要求真实测试输出与交接。
4. 以分支和 Draft PR 交付，记录 head/parent SHA、文件和测试命令/退出码。另有交付 Agent 时单独记录身份。
5. 在全新本机检出验证精确 SHA，比较哈希并跑原测试，不硬重置用户已有检出。
6. Codex 接收脱敏后的核验证据，私人保留审查 JSON 和执行状态。人工核验任务与 SHA。REVIEW_SUCCESS 只是解析到决定，也可能是 REQUEST_CHANGES。
7. REQUEST_CHANGES 按位置、问题、影响、复现、验收条件有限返工。失败、超时、未知阻止推进，保存证据，不无限重试。
8. 仅继续明确授权的下一项。历史两任务记录在 MINI-004 后停止。完成不代表合并、发布、可靠暂停恢复或全天监控。
