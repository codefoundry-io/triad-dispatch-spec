# reference/ — common guidance, written once

Every rule has exactly ONE normative location. Everything else — host `CLAUDE.md` / `AGENTS.md`, skill bodies,
diagrams, tables in plans — points at it. When two places disagree, the location named below wins and the other is a
bug to fix in the same change.

## One source per fact

| Fact | Source of truth (in this repository unless noted) | Derived forms (conform to the source — by hand or by generation; a normative change happens only in the source) |
|---|---|---|
| Result wire: `LegVerdict` fields, enums, finding fields | `contracts/leg-verdict.schema.json` (NOT YET in rev-0 — after the D-3 adjudication round; until then each host's own schema) | host pydantic models; the shape pins inside `prompts/` |
| Leg roster: fields, allowed values, recommended defaults | `contracts/review-legs.example.json` now; `contracts/review-legs.schema.json` (NOT YET in rev-0 — `contracts/README.md`) | host loaders; SKILL text points here |
| Exit tokens and receipt vocabulary | `contracts/exit-tokens.json`; `contracts/receipt-fields.json` (NOT YET in rev-0 — `contracts/README.md`) | host `_common.py` tables, membership-tested against these files |
| Review rules: agreement, correction re-review, roster semantics, Google leg, code-smell criterion, design-change stop, containment, no-cost | `reference/review-rules.md` | SKILL.md rule text (pointers + host invocation syntax), prompt clauses |
| Process flow and failure diagnosis | `reference/process.md` (one diagram) | SKILL flow sections |
| Prompt text | `prompts/*.md` | vendored copies in host skills (vendoring rule: `README.md` § How a host uses a revision) |
| Behavioral cases (inputs, expected results, rule anchor) | `cases/cases.json` | host tests carrying the case ids in their names |
| Which host file implements which surface; which tests carry which cases | `units.json` | none |
| Owner decisions | `decisions/owner-register.md` | quotes in plans and ledgers |
| Revision agreement and signatures | `decisions/rev-N-agreement.md` (rev-1: `decisions/rev-1-agreement.md`) | the relayed round documents point here |
| Which revision a host conforms to | the host repository's `SPEC_REVISION` file | drift reports |
| Gemini read-only policy | `contracts/gemini-readonly.toml` | the host's shipped copy at the adopted revision |
| Measured evidence behind a rule or case change (a spike record: observation with `path:line`, cause chain, the fix on the owning host, the live before/after run, what the other host should touch) | `spikes/<UTC-date>-<slug>.md` | quotes in host plans and ledgers; the case in `cases/cases.json` it produced |

## Anchors

Normative sentences in `review-rules.md` and `process.md` carry stable anchors (`<a id="R-xx"></a>`). Cases and units
reference anchors, never line numbers. Renaming an anchor is a revision.

## Files

- `spec-authoring.md` — how a spec is written and changed in this lab (the method the owner asked to try).
- `review-rules.md` — the rules both hosts implement.
- `process.md` — the shared flow and the failure-diagnosis rules.
