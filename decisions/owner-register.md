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
| D-10 | Reviewer framing adversarial vs neutral: CONTESTED, codex cross-review | `prompts/common-clauses.md § adversarial-framing` |
| D-13 | Host A `fixture.sh` contract: header wins (leak prune + 14-day retention), A-side only | none here |
| D-14 | Untracked symlink in a review tree: CONTESTED, codex cross-review | `R-CLEANUP` (pending) |
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
| Q-W | Google review leg default model = the 3.1 Pro-high tier; Flash retired as a reviewer; the model option stays only so a future model can be evaluated (corrects the leader's "provider default / auto" reading) | `R-NOCOST`, `contracts/review-legs.example.json`, C18 |

Withdrawn at the owner's word: a usage-measurement item (2026-09-19) is not recorded anywhere.
