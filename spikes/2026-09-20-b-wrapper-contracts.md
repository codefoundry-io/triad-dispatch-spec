# B wrapper input and exit-token contracts

Source: B candidate
[`6653bdc4d078dc947c9770660fe68c5690662799`](https://github.com/codefoundry-io/triad-codex-dispatch/commit/6653bdc4d078dc947c9770660fe68c5690662799),
based on the offline v2 foundation `ec3d0df`. Shared authoring input is
`055204c`; latest remote main was fetched before implementation and final review
and remained `2eb883fee59e66556ee7c7f87189b38231136622`.
This is implementation evidence, not a release or revision-adoption claim.

## C8: table parity with preserved producers

The shared contract declares 18 table rows. B lacked `admission-refused`,
`vendor-timeout` and `input-delivery-failed`; its mapper returned fallback exit 1
for them. The independent RED observed exactly those three failures. B now maps
them to terminal exit 65 at
[`bin/_common.py:69–91`](https://github.com/codefoundry-io/triad-codex-dispatch/blob/6653bdc4d078dc947c9770660fe68c5690662799/bin/_common.py#L69-L91).

They remain map-only entries on B. No producer, stdin phase, retry or classifier
repair target changed. `permission-unavailable` remains an inert compatibility
alias; AGY `route-mismatch` retains its explicit direct exit. The exact shared
fixture and tests are
[`tests/test_exit_token_contract.py`](https://github.com/codefoundry-io/triad-codex-dispatch/blob/6653bdc4d078dc947c9770660fe68c5690662799/tests/test_exit_token_contract.py).
The vacuous import-time `is not None` assertion was removed. The bounded literal
census is not an exhaustive data-flow proof: one accepted Minor suggests covering
bare local `classification` assignments. The leader checked the current missed
Claude literal, `extraction-error`, and verified it is already registered.

A already has the three map rows at
[`3rd-Agent/wrappers/_common.py:162–183`](https://github.com/codefoundry-io/triad/blob/92c8afd500499d8736afcc28b39a87a4f87fed50/3rd-Agent/wrappers/_common.py#L162-L183).
A should add the shared membership tests while preserving its active producer
states and phase-specific direct exits. B's map-only assertions must not be
copied over A's active producers.

## C28: loader resolution, separate from evidence custody

B's two helpers formerly rejected relative paths. They now use `pathlib` and
one process-cwd snapshot captured by each wrapper after argument parsing. Both
paths resolve independently from that snapshot; the child's cwd never becomes
the prompt-file base. Existing root/type/existence/UTF-8/XOR/empty checks remain.

Source anchors:
[`_common.py:482–515`](https://github.com/codefoundry-io/triad-codex-dispatch/blob/6653bdc4d078dc947c9770660fe68c5690662799/bin/_common.py#L482-L515),
[`claude_wrapper.py:284–292`](https://github.com/codefoundry-io/triad-codex-dispatch/blob/6653bdc4d078dc947c9770660fe68c5690662799/bin/claude_wrapper.py#L284-L292),
[`gemini_wrapper.py:254–262`](https://github.com/codefoundry-io/triad-codex-dispatch/blob/6653bdc4d078dc947c9770660fe68c5690662799/bin/gemini_wrapper.py#L254-L262),
[`antigravity_wrapper.py:434–436`](https://github.com/codefoundry-io/triad-codex-dispatch/blob/6653bdc4d078dc947c9770660fe68c5690662799/bin/antigravity_wrapper.py#L434-L436).
Tests: `tests/test_wrapper_relative_paths.py`; distinct caller/child file
contents, snapshot stability, absolute/direct callers and pre-provider refusals.
The valid RED observed eight behavior failures and 30 passing controls.

A remains unchanged at `92c8afd500499d8736afcc28b39a87a4f87fed50`. Its matching
helpers still refuse relative paths at
[`_common.py:1148–1190`](https://github.com/codefoundry-io/triad/blob/92c8afd500499d8736afcc28b39a87a4f87fed50/3rd-Agent/wrappers/_common.py#L1148-L1190).
The exact A entrypoints, test and documentation follow-up are linked in
[B's maintainer handoff](https://github.com/codefoundry-io/triad-codex-dispatch/blob/6653bdc4d078dc947c9770660fe68c5690662799/docs/reviews/2026-09-20-wrapper-contracts-claude-handoff.md).

C28 remains PARTIAL: its resolved-path summary/audit requirement and C29 exact
investigation evidence depend on D-B2. Current masking and canonical absolute
review-artifact paths are unchanged. D-B1, v2 dispatch activation, native-host
architecture and dormant B hooks are also unchanged.

## Verification and review

- Dedicated fresh Terra/high RED/GREEN at the canonical source: focused suites
  134 and 49 passed; macOS Python 3.12.13 full suite 1,330 passed.
- Ubuntu 24.04.4 / Python 3.12.3: 1,328 passed, two existing case-insensitive
  filesystem tests skipped. Source/root read-only, network disabled. An initial
  task container used noexec temporary storage; a tiny executable reproduced the
  fixture failure, then correcting that option restored the unchanged suite.
- Source skill validation passed. The fixed provider-free lifecycle ran once:
  SUCCESS, exit 0, all 14 internal commands exit 0, ROUND_INTEGRITY_OK, matching
  source hashes and exact owned-fixture cleanup. The original host completion
  event was recovered after executor display omitted metadata; no rerun was used.
- Round `triad-b-wrapper-contracts-r1`: Claude Opus/xhigh, AGY Pro/high,
  AGY Flash/high and fresh Codex Terra/xhigh all SAFE; canonical admission
  ADMITTED_SAFE with matching final fingerprint. One non-blocking test-census
  suggestion retained on unchanged bytes; no open questions or blocking findings.
  This is B's existing development composition, not a change to the public roster.
- Clean-HEAD Git archive at B `6653bdc`: 1,330 tests passed and all 27 packaged
  file hashes matched. Archive SHA-256:
  `3215c7ad81a9fab5c0c37d79ef5f4f41a25199b67b78155268a3571431d8cc69`.

No live Gemini V1–V5, new model entitlement, installation or release is claimed.
The shared schema/prompt bytes and behavioral expected results are unchanged.
