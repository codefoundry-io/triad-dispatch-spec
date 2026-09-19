# Changelog

## rev-0 (draft; pushed 2026-09-19 at the owner's instruction; not yet tagged) — 2026-09-19

First content from the claude leader after the second agreement round with codex (codex's amendments pending):

- `reference/` — the one-source-per-fact table; the spec-authoring method (owner Q-V: concept only, no UI, no LikeC4);
  review rules with anchors (agreement per owner Q-S, correction re-review, roster per Q-L/Q-M/Q-O, Google leg per Q-N,
  smell criterion, design-change stop, containment inventory with the two verified A-side defects, no-cost/CLI-only with
  the `--policy` and auth-vs-model source findings, platforms); the shared process diagram (codex's second-pass shape) and
  the four failure-diagnosis rules.
- `prompts/` — host A's shipped review text split into a shared clause library + leg-specific clauses with an order list
  (owner Q-U; no clause appears twice); host B's counterpart to be merged by codex from `render_review_prompt`.
- `contracts/` — A's `gemini-readonly.toml` with the header expanded by the version-pinned `--policy` source cite (A's
  substance was right); A's exit-token table as data with the B delta to confirm; a post-cut roster example.
- `cases/cases.json` — C1–C24 seed with rule anchors (C19–C24 added after the fresh-eye check); host test columns partly
  filled (A), B to fill.
- `units.json` — surface → common shipped name → contract → preserved host exceptions → host paths.
- `decisions/owner-register.md` — owner rulings and their effect, site-neutral (verbatim record stays in the host plan).

Amendment 2026-09-19 (owner Q-W): Google review leg default model = the Pro-high tier on either CLI; Flash retired as a
reviewer; the model option is kept only to evaluate future models (`R-NOCOST`, roster example, C18).

Read by: claude leader (author) · codex leader — pending · owner tag — pending.

Roster keys deliberately ABSENT in v2 (audit ranks 1-10, owner Q-M/Q-N/Q-O): `substitute_for`, `operation`, `posture`,
`trial`, `sites`; no `legs` subcommand; `vendor` is a family value (`claude` | `codex` | `google`) and the Google CLI is
named only by the `agy` / `gemini` block.
