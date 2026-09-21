# Host A finding: a skipped enabled entry has no specified outcome when a same-family sibling completes

Status: PROPOSAL from the Claude host maintainer, on a local branch. Not merged,
not published, not a revision tag, and not an owner decision. It records a gap
found by running case C33's four-leg profile for real.

## How it was found

Host A ran the owner's four-leg profile (one codex entry, three named Google
entries) as gate-1 round r11 on 2026-09-22. The round collected
`BLOCKED entries=4/4 families=2 blocking=19`. One Google leg raised, as a
Critical, that A's collector drops a SKIPPED enabled entry from the set it
folds, so with three same-family entries a skipped sibling is invisible: the
family stays covered by the other two and the round can still reach agreement.

Cross-checking the codex host settled A's own answer and exposed the gap:

| Host | Behaviour | Evidence |
|---|---|---|
| A (claude) | route resolution SKIPS an unusable Google entry and logs it (R-GOOGLE); the collector then folds only the dispatched entries, so the skipped one contributes nothing to the outcome | `lib/roster_v2.py` `_resolve_google`; `lib/collect_v2.py` `_dispatched` / `_outcome` |
| B (codex) | `collect` iterates EVERY enabled entry and sends any entry without a COMPLETE terminal to `missing`, which forces `INCOMPLETE`; separately, an enabled entry that cannot launch is a PREPARATION REFUSAL, so the state cannot arise | `bin/review_round_v2.py:505-530`, `:160` (released v0.2.556 at `5a12f82`) |

B is right and A is wrong, and A is fixing its own code. The gap is that the
SHARED RULES do not decide it.

## The gap

- [R-GOOGLE](../reference/review-rules.md#R-GOOGLE) sanctions A's "skip and log"
  at route resolution and records that the neither-installed outcome differs by
  host (A skips, B refuses).
- [R-AGREE](../reference/review-rules.md#R-AGREE) says a missing, failed,
  invalid or unresolved non-affirmative result is not agreement.

Neither states what the OUTCOME must be when a skipped enabled entry's family is
still covered by a same-family sibling. That state could not arise while every
family had exactly one entry: a skipped Google leg removed the Google family, and
family coverage carried the signal. Case C33's three Google entries create it.
A read the two rules together as "skip, then drop"; B never reaches the state, so
its correctness here is a by-product of refusing earlier, not of a rule.

Fixing only A's code leaves the next host free to repeat the same reading.

## Proposed clarification (wording, not adopted)

> A skipped enabled entry is a MISSING RESULT for outcome purposes on every host.
> It is counted, it is named in the round record, and it makes the round
> INCOMPLETE whether or not a same-family sibling completed. Family coverage is
> never a substitute for an entry that was enabled and did not run. A host that
> refuses such an entry before dispatch satisfies this by construction.

Suggested home: a sentence in R-AGREE (it already owns "a missing result is not
agreement") with a pointer from R-GOOGLE's skip branch, plus one line in case
C33's `expected` so the behaviour is testable rather than inferred.

## Boundary

No rule, schema, prompt clause, policy payload or default roster is changed by
this document. Host A's own fix is in its gate-1 fix wave; this proposal exists
so the rule, not just one implementation, carries the answer. Publication,
merge and any revision tag remain the owner's decision.
