# B cleanup entry evidence: existing R-CLEANUP, C4/C69 and DL-77

Read-only basis: B5f5dda5b plus the U1T candidate, shared d082a60, A59fbfd1.
This records a demonstrated source difference before U6 design/implementation;
it adds no deletion capability, new normative rule or native-leg requirement.

B `bin/_common.py:2879` creates fallback run-log directories without an
allocation marker. Its `prune_stale_run_logs:3031` calls
`prune_stale_tmp_dirs:3071`, which checks only a prefix and directory age before
recursive removal. Existing `test_next_run_prunes_stale_fallback_ipc_directory`
expects that behavior. R-CLEANUP requires ownership proof, never a name shape.

An isolated synthetic fixture reproduced the current behavior: an old folder
named `triad-gemini-run-log-foreign`, containing a sentinel and no ownership
proof, was removed; an old different-prefix folder and a fresh matching-prefix
folder survived. The helper was explicitly given the fixture's base; no real
system temporary-folder sweep or provider call ran. The same invocation removed
its exact fixture. This proves a code/contract difference, not an actual incident
of lost user data. B evidence: workspace
`_runs/infra/20261010-spec-to-code/u6-name-proof-spike.json`.

B's existing review-packet cleanup has separate allocation identity, verified
export, interrupted-removal subset checks and proof-last deletion. Preserve that
working mechanism. Its declared-root configuration gap is already DL-77; a new
general deletion framework is not justified merely by this temporary-folder bug.

A source provides a shared-schema default configuration and host deletion code
in `3rd-Agent/wrappers/cleanup.py` and `cleanup-roots.default.json`. Its project
override, linked-worktree mechanism and one-day run-log floor remain A-owned.
B's one-hour run-log floor and thirty-day review sweep are its own data. B did
not execute A's cleanup or claim complete current A conformance.

Next B work: settle its root/proof declarations and preserve old unmarked residue
before changing the sweep; create fresh provider-free ownership/age/interruption
tests and complete the normal unit review. Reuse existing entry points where
possible. A new public interface or material migration choice requires the owner;
no such interface is selected in this evidence record. U8 installation coexistence
remains withdrawn and is not a cleanup prerequisite or renamed task.

## Diagnosis and bounded sequence

Claude opus/xhigh, Google Pro/high and fresh Codex Astra/high independently
confirmed the reachable missing-proof path. B checked their suggestions against
source: extension-only unlink is not ownership, and the obsolete codex fan-out
docstring describes no current caller. No background service, new public
deletion command or A-native port is justified. B's cleanup tests also need
isolated temporary bases for both pytest and their standalone runner.

U6a will correct this fallback allocation/sweep using an exact-directory
allocation record, proof-last interruption handling and preservation of old
unmarked residue. U6b separately owns the declared-root/floor migration and
normal sweep/cap/archive entry points. U6a alone will not close DL-77 or claim
all C69 behavior. Existing review export/identity/subset guards stay intact.

Current-source refresh: main3afc4d7, PR12 11934f11, read-only A0be173bf (clean).
A's intervening documentation/comment cleanup changes no relevant model or
cleanup runtime path. No A execution or cleanup-conformance claim is made.

The cleanup schema's `min_age_s` description was broader than the normative
R-CLEANUP paragraph: the latter already exempts an explicit named-round close
and resumption of a deletion already decided. The description and C69 boundary
now point to that existing exception; no new age policy, proof bypass or typed
surface is introduced. Allocation/ownership requirements remain unchanged.
