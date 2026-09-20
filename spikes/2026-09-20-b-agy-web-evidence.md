# B: restore the authorized AGY investigation evidence procedure

## Basis and ownership

Remote `main` fetched on 2026-09-20: `2eb883fee59e66556ee7c7f87189b38231136622`.
Shared authoring basis: `1fb2de9e974e050804dcd4f3ec2adb629f83b6a9`.
B: `56f0f6657084f81516217ee51698f9b18cfc71dc`.
A (read-only): `92c8afd500499d8736afcc28b39a87a4f87fed50`.
The owner reaffirmed that yesterday's AGY page-fetch defect is delegated to B
for repair and testing. The clarification does not request an audit-redaction
change. This implements existing C29/R-INVEST, not a REVIEW web exception.

## Evidence and current behavior

The [original spike](2026-09-19-google-web-evidence.md) records search-only
answers, unfetched citations and one bounded before/after experiment showing
improvement with the shared clause. That experiment does not prove B behavior
or a general failure rate. B `bin/antigravity_wrapper.py:402-448` lacks `--web`
and the clause. Its dispatch at `:652-676` and custody call at `:704-711` use
the same local prompt. A already appends its clause after validation at
`3rd-Agent/wrappers/antigravity_wrapper.py:1381-1393`; its clause is at `:294`.

## B change and preserved functionality

- Add explicit `--web` for raw INVESTIGATION only; require `--sandbox read-only`.
- Reject blank caller prompts and formal/preflight combinations before provider
  work. Load the single fenced clause from a byte-identical vendored
  `prompts/investigation.md` only for the authorized operation; append one blank
  line and that clause without trimming caller bytes.
- Pin the vendored document and digest in a separate prompt provenance manifest;
  do not alter the independently pinned candidate schema bundle or revision adoption.
- Reuse existing command construction, guard, schema, audit and failure-log paths.
  They receive the final prompt. Hardened masking and failure-only run-log behavior
  remain unchanged. Do not claim that redacted success logs retain full prompt bytes.
- Preserve no-flag behavior, arbitrary optional schemas, read-only mutation denies,
  existing owner denies, auth, process cleanup and REVIEW no-web behavior.

No common normative clause or case expectation changes. D-B2's proposed new
custody destination is not implemented; complete C29 durable-custody conformance
is not claimed by this behavioral repair.

## Verification and Claude handoff

Before production edits: dedicated fresh Terra/high RED; then smallest fix and
separate fresh GREEN, full macOS/Ubuntu 24.04 regressions, packaged byte equality,
and required full-scope multi-family review. A live AGY 1.2.7 Pro/high investigation
will retain the sent prompt and raw stream in the explicitly scoped spike output.
The leader compares completed page-fetch events with every answer citation and
independently checks the cited source. Prompt instructions alone are not proof.

Claude leader: review this same shared commit and the subsequent B evidence.
Keep A unchanged while B leads. A's existing append is already present; compare
the live fetch/citation result and any new failure cause before applying changes.
Do not copy B's native plan-mode adapter into A's custom research-agent route.
Implementation and live results are pending; this document records the work
before B changes its source.
