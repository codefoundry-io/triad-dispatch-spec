# Owner decisions — rulings and their effect (public, site-neutral)

This repository is public. Each row records WHAT the owner decided and WHERE it lands here; the owner's exact words
(Korean, verbatim) are kept in the claude host's working record (`triad` plan `2026-09-19-triad-host-parity-plan.md § 8b`)
and in codex's consolidated document for the directions given in codex's session. Where the owner selected an option the
leader had written, the row says "selected option"; the choice is the owner's, the label the leader's. Nothing here is a
new rule; every row points at the normative location.

| ID | Decision | Effect here |
|---|---|---|
| D-3 | Verdict wire contract: adjudicate via ONE three-family round, each host keeps its own schema until then | `contracts/leg-verdict.schema.json` NOT YET; `R-AGREE` last sentence |
| D-4 / Q-L | Three-family review is the default; substitutes are contingency; the model behind each slot is replaceable; at least three legs run | `R-ROSTER` |
| D-9 | Network tools in the gemini review policy: same three-family round, date-anchored web evidence only | `contracts/README.md` (policy row) |
| D-10 | Reviewer framing: CLOSED by owner Q3 (codex session) — evidence-centred, a no-defect conclusion allowed | `prompts/common-clauses.md § adversarial-framing` |
| D-13 | Host A `fixture.sh` contract: header wins (leak prune + 14-day retention), A-side only | none here |
| D-14 / Q4 | RULED 2026-09-19: "링크 자체는 검토하되, 대상을 자동으로 따라가지 않는 방식" — the link itself is reviewed (text fingerprinted, visible); the target is never followed automatically; mechanism per host | `R-PREPARE`, C26 |
| Q-A | The host where gemini is in service can download from GitHub but not upload | `README.md § How a host uses a revision` (owner pushes; results come back by briefing) |
| Q-B / Q-H / Q-Q | Agreement = no unresolved BLOCKING finding from any leg; tiers are data | `R-AGREE`, `R-ROSTER` |
| Q-C | A leg that failed to RUN with nothing changed is retried alone | `R-RETRY` |
| Q-D | A selected investigation returns a free-form report, never a review verdict | `R-ROSTER` last sentences |
| Q-E / Q-M | No "degraded" label ceremony; no per-leg special rules; a leg has a recommended default model, changeable anytime; the count is variable | `R-ROSTER` |
| Q-F / Q-K | No development before the design spec is agreed; approved defect fixes on host A continue | `README.md` (rev-0 is a draft, not implementation authorization) |
| Q-G / Q-J / Q-N | agy and gemini are distinct CLIs of one family with opposite availability at the two sites; keep each host's SHIPPED fallback logic; the owner tests gemini where it is in service and briefs the leader | `R-GOOGLE` |
| Q-O | `acceptance` is a data field only; every rule derived from it is cut | `R-ROSTER`, `contracts/review-legs.example.json` |
| Q-P | The shared package lives in this SEPARATE repository; enforcement mode is the leaders' call (recommendation: informational drift report first) | `README.md § How a host uses a revision` step 3 |
| Q-S | selected option: a MERGE WITH FIXES with only Minor findings counts as agreement, no extra round | `R-AGREE` |
| Q-T | selected option: leaders hand files, the owner pushes | `README.md` step 1 and 4, `AGENTS.md`/`CLAUDE.md` |
| Q-U | selected option: prompts live here as the one editable copy; hosts vendor at the adopted revision | `prompts/`, `README.md` step 2 |
| Q-V | Concept only, no UI, no LikeC4; this repository is a lightweight experiment lab | `README.md` purpose, `reference/spec-authoring.md § 7` |
| Q1 (codex session) | selected option: "코드를 수정하면 전원 재검토. Minor만 남은 원본은 승인 가능" — Minor-only findings do not block the unchanged reviewed bytes; any change to reviewed content = full participating-roster re-review | `R-AGREE`, `R-REREVIEW` |
| Q2 (codex session) | selected option: "두 CLI 모두 Pro 계열 + 확인 가능한 high로 맞춤; 인증 경계 유지" — Pro family + verifiable HIGH on both Google CLIs; B's Auto-only path and A's unpinned gemini call = migration items | `R-NOCOST`, roster example, C18 |
| Q3 (codex session) | selected option: "증거 중심으로 통일하고 무결함 결론도 허용" — shared review prompt is evidence-centred and allows a no-defect conclusion; D-10 closed | `prompts/common-clauses.md § adversarial-framing` |
| Q-W | Google review leg default model = the 3.1 Pro-high tier; Flash retired as a reviewer; the model option stays only so a future model can be evaluated (corrects the leader's "provider default / auto" reading) | `R-NOCOST`, `contracts/review-legs.example.json`, C18 |

| D-3 (round r2) | Three families converged on a superset v2 wire (`contracts/leg-verdict-mapping.md`); residual choices are leader-level | `R-AGREE` open-question axis, `R-BIND` v2 additions |
| D-9 (round r2) | CONFLICTED: codex and google recommend ALLOW web tools in review legs with a date + version anchor; claude recommends DENY by explicit rows (and found A's policy INHERITS a search allow today). Owner decision requested | `contracts/gemini-readonly.toml` header, `contracts/README.md` |
| Q4 (round r2) | Split 2:1 (materialize in the round copy vs fingerprint + no-follow clause) → owner ruled the PRINCIPLE (review the link itself, never follow the target automatically); the mechanism is each host's migration item | `R-PREPARE`, C26 |

| Directive (2026-09-19) | The recurring relative `--prompt-file` dispatch failure must be solved mechanically, not by instructions: resolve against the caller's cwd or align the path with cwd; record the problem in the plan and specify the fix | `R-CONTAIN` (all wrappers), C28; host plan P4-22 |

Withdrawn at the owner's word: a usage-measurement item (2026-09-19) is not recorded anywhere.
