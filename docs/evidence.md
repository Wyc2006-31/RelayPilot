# Evidence / 证据分级

Preparation date / 整理日期：2026-11-04 (Asia/Shanghai).

| Evidence / 证据 | Classification / 等级 | Result / 结果 |
|---|---|---|
| MINI-001 exact local Git snapshot | locally rerun / 本机复跑 | 11 tests pass / 11 项通过 |
| MINI-002 exact local Git snapshot | locally rerun / 本机复跑 | 11 converter tests; CLI smoke / 11 项转换测试及 CLI 冒烟 |
| MINI-003 exact local Git snapshot | locally rerun / 本机复跑 | 24 tests pass / 24 项通过 |
| MINI-004 exact local Git snapshot | locally rerun / 本机复跑 | 35 tests pass / 35 项通过 |
| Four original review JSON records | HISTORICAL_RECORD | APPROVE tied to recorded commit; not rerun / 关联记录提交，未重新调用模型 |
| One trigger, two tasks | HISTORICAL_RECORD | local state/report and PR chain; no new trigger / 历史状态报告与 PR 链，本次未触发 |
| Candidate demo | locally rerun / 本机复跑 | 35 original tests; unchanged Python blobs / 原 35 项与未改 Python blob |
| Launcher safety preflight | offline / 离线 | 3 tests; no model call / 3 项，不调用模型 |
| Full fresh cloud relay / 全新云端接力 | UNVERIFIED | exact portable Routine/UI run not supplied / 缺精确可移植 Routine 与完整 UI 复跑 |

Initial local runs with UTF-8 output but GBK parent decoding failed in MINI-003/004; setting PYTHONUTF8=1 resolved the environment mismatch without source edits. Failed logs are retained privately. Counts overlap and cannot be summed as unique tests. No claims of performance, model identity or production deployment follow from these tests. Private evidence identifiers and logs are intentionally excluded from publication.

首次 UTF-8 输出配 GBK 父进程读取使 MINI-003/004 失败；PYTHONUTF8=1 统一编码后通过，未改源码，失败日志私人保留。版本测试有重叠，不累加；测试不证明性能、实际模型或生产部署。私人证据标识和日志不进入发布包。

## Preview acceptance is separate / 预览验收独立

For this documentation refinement, existing original-workflow evidence is reused; no MINI-003/004 workflow is triggered again. `HISTORICAL_VERIFIED` may describe the **earlier independently rerun exact code snapshots and checks**, not an unobserved cloud action. Historical review JSON remains `HISTORICAL_RECORD`: its existence and recorded SHA/decision are readable, but the model call is not rerun. The single-trigger claim remains a historical state/report claim; **fresh, independent reproduction of that automation is UNVERIFIED**. The presence of a report alone is not sufficient to promote a cloud capability to HISTORICAL_VERIFIED.
本轮复用原证据，不重触发 MINI-003/004。HISTORICAL_VERIFIED 仅可描述上一轮独立复跑过的精确代码快照与核验，不用于未观察的云动作。审查 JSON 仍为 HISTORICAL_RECORD：能读到记录的 SHA/决定，但未重新调用模型。单触发是历史状态/报告中的记载，新环境独立自动化复现仍为 UNVERIFIED；报告存在不足以把云能力升级为 HISTORICAL_VERIFIED。

**A — experimental Preview review:** evaluate the included local program, readable instructions, explicit limitations and applicable safety checks. **B — full automated deployment:** additionally requires portable platform setup, authenticated trigger/return/continuation, live handoff and recovery evidence. Passing A does not assert B. See [draft Preview release scope](release-notes-v0.1.0-alpha.1.md).
**A 实验预览审核：**检查已包含的本机程序、可跟随教程、明确限制与必要安全检查。**B 完整自动部署：**另需可移植平台配置、认证触发/回传/继续、真实交接和恢复证据。A 通过不代表 B，通过范围见预览发布说明。
