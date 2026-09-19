# How specs are written in this lab

Adapted from the owner's Spec Rebuild Lab blueprint (2026-09-19) to a documentation-and-contracts repository with no
application code: no UI, no LikeC4, no generated docs (owner Q-V). The point is that a fact is decided once, written
once, referenced everywhere, and tested by cases that accumulate.

## 1. The three things a human approves

1. **Who talks to whom** — the surfaces: file names, subcommands, options, prompt files, receipt fields, tokens.
2. **What result is correct** — behavioral cases: input, expected result, the rule it proves.
3. **What may not change without a revision** — the frozen surfaces: contracts, prompt files, the rules' normative text.

Everything else (how a host implements a surface, its internal test tree, its install layer) is the host maintainer's.

## 2. The authoring conversation (one decision at a time)

When a rule or surface is added or changed, the author answers these questions before writing; the answers go where the
table says. A question the owner already answered is not asked again (`decisions/owner-register.md`).

| Question | Where the answer lives |
|---|---|
| What does a maintainer or a reviewer observably get? | `review-rules.md` / `process.md` normative sentence with an anchor |
| Which existing surface is reused (file, option, token, prompt clause)? | a reference to `contracts/` or `prompts/`, never a copy |
| Which host files may change for it, and who owns them? | `units.json` row |
| Does it call a vendor, read outside the review tree, use a clock, or network? | the containment section of `review-rules.md` |
| One normal example and one failure or boundary example? | `cases/cases.json` entries (before any host code) |
| What is still ambiguous? | an owner question, asked in advance, recorded verbatim |

## 3. Writing rules

- One normative location per rule, with an anchor. Other documents point; diagrams navigate; tables summarise with a link.
- Types live in schemas (`contracts/*.schema.json`), not in prose; prose describes, the schema decides.
- Owner decisions are quoted verbatim; a leader's option label is marked as such.
- A "must survive" list cites the host file and symbol that ships the guard today.
- No per-leg special rules, no ceremony fields: a leg is an entry with recommended defaults (owner Q-M).
- Prompts are files, one clause per rule, editable by the owner without touching code; hosts vendor them at the revision
  they adopt (owner Q-U; vendoring rule: `README.md` § How a host uses a revision). A host skill body carries invocation
  syntax and pointers, not the clauses.

## 4. Cases accumulate; they are never weakened

```
defect or ambiguity found (any host, any round)
→ reproduce it against the reviewed bytes
→ write the case FIRST: id, rule anchor, input, expected — in cases/cases.json
→ the owning host fixes and names its test after the case id
→ the other host runs the same case at its next conformance run
→ the case stays; the rule text gains the anchor if it lacked one
```

A case that fails is a defect in the host or in the spec, never a reason to change the expected result without a
recorded decision. An unrun case is listed NOT RUN, never green. A refuted finding is recorded in the round ledger, not as a
case.

## 5. Revisions

A revision (`rev-N` tag) is the freeze: after it, changing a contract, a prompt file or a normative sentence is a new
revision with a `CHANGELOG.md` entry naming the anchors, cases and units it touches. The owner tags after the other
leader has read the change (owner Q-T).
Hosts adopt explicitly (`SPEC_REVISION`) and may lag; the drift report lists which revision each conforms to and which
case ids are red.

## 6. What code does and what AI does

- Code (deterministic, thin, added only when a repeated manual check exists): a `spec-check` that resolves every anchor,
  case id and unit reference; a digest check that a host's vendored prompt or contract equals the source at the adopted
  revision. Neither exists yet; they are described so the first one is small.
- AI: detecting ambiguity while authoring, reviewing a rule's meaning, judging a finding semantically. AI never decides a case's pass/fail; deterministic schema and integrity validation is code.

## 7. Not in this lab (rev-0)

LikeC4 or any architecture GUI; generated documentation; cross-host release gates; synchronized releases; a contract
"controller" role. Any of these needs an owner decision and a recorded reason.
