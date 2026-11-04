# RelayPilot Gen 1 | First Experimental Preview

**v0.1.0-alpha.1 · Pre-release · First Generation / 第一代实验预览版**

This is RelayPilot's first-generation experimental preview: a real, inspectable workflow reference that can be learned, adapted and reproduced progressively. It includes a local temperature example, the original 35-test suite, a configurable historical Codex review launcher, bilingual setup/manual relay docs and offline preflight checks. The original private runtime remains separate. Full cloud reproducibility, strict model enforcement and automatic recovery remain unverified or planned. Future releases will continue to improve, refine and update this workflow.

这是 RelayPilot 第一代实验预览：真实可学习、可参考、可逐步复现的工作流公开版本，包含本机温度示例、35 项原测试、可配置历史 Codex 审查启动器、双语安装/人工接力文档和离线预检。原私人运行系统独立保留。完整云端复现、模型强制机制与自动恢复仍待验证或规划；后续会继续同步优化、迭代和更新工作流。

## Verified / 已验证内容

- The local example passes 35 original tests; three offline preflight tests check launcher setup without model calls. CLI examples and invalid-input exit codes are checked from a clean source directory.
- Windows/Ubuntu × Python 3.11/3.13 CI validates these offline suites. This is not cloud-agent or model execution evidence.
- Exact Git commits, file hashes, test records and review decisions are documented as handoff evidence. Historical MINI records remain historical; no new automated cloud run is claimed.

- 本机示例 35 项原测试与 3 项离线预检通过；干净源码目录核验 CLI 输出和错误退出码。
- Windows/Ubuntu × Python 3.11/3.13 CI 验证离线测试，不证明云 Agent 或模型调用。
- 文档以精确提交、文件哈希、测试记录和审查决定解释交接；原 MINI 记录仍为历史证据，不冒充本次云端自动运行。

## Who this is for / 适合谁使用

Developers learning multi-agent collaboration, readers studying an evidence-based coding process, and experimenters who can configure their own tools and manually validate handoffs. Start with the local demo; cloud services are optional and require your own accounts, permissions and cost decisions. This is not a production-ready commercial automation service.
适合学习多 Agent 协作、研究可核验编程流程，以及能自行配置工具并人工核验交接的开发者。先跑本机示例；云服务是可选扩展，需自己的账号、权限和费用决策。这不是可直接用于生产的商业自动化服务。

## Preview scope / 第一代预览范围

This Preview is useful for developers who want to run a small genuine coding deliverable and inspect a multi-agent handoff reference. Start with the [local tutorial](preview-quickstart.md): converter functions, the original CLI with optional `--to`, 35 original tests and 3 offline launcher preflight tests are included. The historical Codex launcher is configurable but its real provider execution is not newly validated. No accounts, original state or cloud tools are needed for the local tutorial.
本预览供开发者运行真实小型编程产物，并了解多 Agent 交接方法。包含转换函数、带可选 --to 的原 CLI、35 项原测试和 3 项离线预检。历史 Codex 启动器可配置，但未重新验证真实 provider 执行。本机教程无需账号、原状态或云工具。

## Manual setup / 需要人工配置

The optional [manual relay](manual-relay.md) requires separately installed tools, your own provider login/key and route, your own WorkBuddy task/workspace, an authorized sandbox GitHub repository, verified SHA handoffs and manual review linkage checks. Grok Bot requires the correct distribution/feature access and its own supported Routine/Webhook configuration. The original portable export/trigger-return schema is unavailable, so that automatic integration is UNVERIFIED. No fabricated import/API or one-click deployment is supplied.
可选人工接力需独立安装工具、自己的提供商认证和路由、WorkBuddy 任务/空间、授权沙箱仓库、精确 SHA 交接及人工审查关联。Grok 还需正确发行版/权限及其支持的 Routine/Webhook 配置。原可移植导出和触发回传 schema 未取得，自动集成为 UNVERIFIED；不提供虚构导入/API 或一键部署。

## Two independent decisions / 两项独立判断

| Decision / 判断 | Gen 1 Preview meaning / 含义 |
|---|---|
| A: experimental open-source Preview / 实验开源预览 | The owner has approved publishing the safety-reviewed local/reference scope. This approval does not assert full cloud reproducibility. / 所有者已批准公开经审查的本机与参考流程范围，不代表完整云端可复现。 |
| B: complete end-to-end automated deployment / 完整端到端自动部署 | **No / UNVERIFIED.** No portable original Routine, independently replayed cloud trigger/return chain, reliable automatic model fallback or recovery deployment. / 尚无原 Routine 可移植导出、新云触发回传链独立复现、可靠自动模型切换和恢复部署。 |

Earlier BLOCKED_FOR_REPRODUCIBILITY reports remain valid historical assessments of **B**. The refined **A** gate narrows the Preview's advertised scope; it does not retroactively claim the original cloud blocker was fixed. Original MINI history is preserved, not rerun or relabeled as a fresh cloud success.
此前 BLOCKED_FOR_REPRODUCIBILITY 报告保留为 B 的历史判断。本轮明确 A 的预览宣传范围，不声称原云端阻塞已修复；保留原 MINI 历史，不重跑或改称本轮云成功。

## Known limits / 已知限制

The launcher retains permissive JSON parsing, manual task/SHA linkage, raw private logs and direct-child-only timeout termination. A parsed REQUEST_CHANGES can still produce REVIEW_SUCCESS; exit 0 is not approval to advance. UI model labels do not attest the served model; 429 handling and automatic selection are not reliable implemented guarantees. Read [all retained limitations](limitations.md) before real use. No automatic merge, release, visibility change or social publishing is included.
启动器保留宽松解析、人工任务/SHA 关联、原始私人日志和仅终止直接子进程的超时机制。解析到 REQUEST_CHANGES 仍可能为 REVIEW_SUCCESS，exit 0 不授权推进。模型 UI 标签不证明服务模型，429 处理和自动选型未形成可靠已实现保证。真实使用前阅读全部限制；无自动合并、Release、改可见性或宣传发布。

## Next / Gen 1.1 后续

**PLANNED Gen 1.1:** strict review-to-commit checks, model-selection evidence, bounded rate-limit behavior, task idempotency/state and recovery; validate a portable platform recipe when available. **PLANNED Gen 1.2:** installation, configuration and private logging/monitoring. **PLANNED Gen 2:** more agents and visual task management. Existing working behavior and tests must be retained; none of this roadmap is asserted complete.
**PLANNED Gen 1.1：**严格审查提交关联、模型选择证据、有界限流处理、任务幂等/状态与恢复，并在条件具备时验证可移植平台配方。**PLANNED Gen 1.2：**安装、配置、私人日志/监控。**PLANNED Gen 2：**更多 Agent 和可视化任务管理。保留原功能测试，以上均未声称完成。
