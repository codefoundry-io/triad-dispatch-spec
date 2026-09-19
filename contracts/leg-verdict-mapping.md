# LegVerdict — A↔B mapping and the proposed v2 wire (round r2 output, 2026-09-19)

Three families (codex, google/agy, claude fresh-eye) adjudicated D-3 independently and converged: a SUPERSET wire, not a
collapse. Host facts: A `verdict_schema.py` (3 verdicts, 4 severities, `context_known`), B `verdict_schema.py` (SAFE /
NOT-SAFE, 3 severities, `affected_surfaces_inspected`, `open_questions`; any open question ⇒ NOT-SAFE).

## Mapping and losses

| Item | A | B | A→B loss | B→A loss | v2 |
|---|---|---|---|---|---|
| verdict | SAFE TO MERGE / MERGE WITH FIXES / DO NOT MERGE | SAFE / NOT-SAFE | "fix then land" vs "must not land" collapses into NOT-SAFE | NOT-SAFE cannot be split back | A's three; `SAFE` is an import alias only; uncertainty-only negative = DO NOT MERGE + nonempty open_questions; no fourth token (aligned below) |
| severity | Critical / must-fix / Minor / HARDENING-SUGGESTION | Critical / Major / Minor | HARDENING-SUGGESTION lost | Minor ambiguous | A's four; `Major` = import alias of must-fix |
| path field | `file` (repo-relative, python validator) | `path` (JSON-Schema pattern) | rename | rename | `path` + B's schema-level pattern so the vendor's own schema check rejects absolute paths (aligned below) |
| line | int ≥ 1 or null | same | — | — | same |
| summary | required | — | lost | must be synthesized | keep, required |
| trigger | required | required | — | — | same |
| evidence | — | required | — | lost | required (the Q3 evidence-centred ruling made mechanical) |
| correction | — | required | — | lost | OPTIONAL (required would contradict R-VERIFY: labels are claims, not repair instructions) |
| context_known | required bool | — | lost | — | keep |
| criteria_checked | required, unique | required, unique | — | — | same |
| affected_surfaces_inspected | — | required, unique, path-constrained | not constructible from A | lost | required for newly authored v2 results |
| open_questions | — | required list, may be empty; any entry ⇒ non-affirmative | not constructible | unrepresentable (A rejects a finding-less non-SAFE) | required list; any unresolved entry blocks (R-AGREE) |
| binding | review_id, family, content_digest | same | — | — | + `leg_name`, `attempt` (≥ 1, per leg), `route` (agy \| gemini, null for one-route families), `schema_version: 2` |

## Release properties that must survive (all three legs)

1. A's Minor-only release on UNCHANGED bytes (owner Q-S / Q1): a non-affirmative verdict carrying only Minor findings and
   no open question is VALID and recorded as a verdict-selection deviation — never a schema rejection (B's validator must
   relax here).
2. A's verdict-selection discipline survives as PROMPT guidance, not as a schema invariant.
3. B's open-question rule survives: any unresolved open question makes the result non-affirmative; an uncertainty-only
   negative needs no invented finding. A's "non-SAFE requires a finding" relaxes to "a finding OR an open question".

## Invariants of the proposed v2 object

(i) SAFE TO MERGE ⇒ no Critical / must-fix finding AND `open_questions` empty. (ii) non-affirmative ⇒ at least one finding
OR one open question. (iii) a non-affirmative object whose findings are all non-blocking and whose `open_questions` is
empty is VALID (property 1). Unknown fields and duplicate members are rejected at the original-text boundary on both hosts.
Legacy results are never converted into fabricated evidence, coverage or an empty uncertainty list — a missing v2 field
stays absent/unknown, and a converted result is not admissible under v2 without a new review.

## Migration notes (refuters)

Both hosts' models are `extra="forbid", strict=True`: every v2 field is a breaking change for BOTH validators — the flip is
one slice per host, landed with EVERY schema-shaped prompt clause in the same change — `prompts/common-clauses.md § severity-instruction`,
`§ verdict-selection-rule`, `leg-claude.md § claude-verdict-shape` AND `leg-google.md § google-findings-shape-pin` (today it pins the six
v1 finding fields; v2 requires `evidence`, so the old pin would instruct a reviewer to omit a required field — codex F6) — plus both B
renderers, both hosts' validators and their fixtures. B has no NONREPAIRABLE gate but runs
one schema-repair retry; A's nonrepairable-blocker exception stays host-local.

## Aligned leader-level choices

ALIGNED 2026-09-19 (both leaders, co-review; no owner decision needed): the one path field is `path`; the three canonical verdicts are
A's (`SAFE` and `Major` survive as IMPORT aliases only, never emitted); `correction` is optional; an uncertainty-only negative is
`DO NOT MERGE` with a nonempty `open_questions` and no invented finding — no fourth `NOT-SAFE` token; a legacy result is kept as
evidence and never converted into fabricated coverage, context or evidence — a v2 review is a fresh review. The schema file
`contracts/leg-verdict.schema.json` is written from this section (still NOT YET).
