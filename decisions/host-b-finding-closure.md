# Host B original NOT-SAFE finding register

Original round: `host-b-start-audit-r1`, 25 findings across Claude, Google and
fresh Codex. IDs below are reviewer-local positions, not shared behavioral case
IDs. The full diagnostic basis and source adjudication are in
[the preimplementation audit](host-b-preimplementation-audit.md).

This register tracks correction and full fresh review. A green P1 review cannot
close non-P1 findings. No prior approval carries forward after reviewed bytes or
conditions change. No row is closed merely because it has a planned correction.

| IDs | Disposition / bounded plan | Verification and status |
|---|---|---|
| claude-02, claude-08, google-02, codex-02, codex-04 | P1: C1/C2 terminal transport and C6 completed-result custody | CLOSED at B `e29d820fb4fb35b64fc9e955aee5357377f23418`. Fresh RED/GREEN plus corrected full round `triad-b-p1-r2`: all four SAFE, matching integrity, ADMITTED_SAFE. macOS 1042 passed; Ubuntu 24.04 1040 passed, 2 filesystem skips. [PR 27](https://github.com/codefoundry-io/triad-codex-dispatch/pull/27) is a separate integration state; deployment not claimed. [Spike](../spikes/2026-09-20-b-terminal-custody.md). |
| claude-03, google-01, codex-03 | P2: allocation provenance and verified export before cleanup | CLOSED in source `a85a8006c671da94c5a4f7c49a3c9e0acb12cc5c`, full round `triad-b-p2-r2` ADMITTED_SAFE; [B PR 28](https://github.com/codefoundry-io/triad-codex-dispatch/pull/28). macOS 1081, Ubuntu 1079 + 2 skips; exact evidence custody and cleanup verified. [Spike](../spikes/2026-09-20-b-owned-cleanup.md). |
| claude-06, codex-05 | P3a: original JSON duplicate rejection and reserved verdict binding completeness | CLOSED in source `bc9ff6949d165e1c11edb44ef1ad519bdaeb40dc`, full round `triad-b-p3a-r2` ADMITTED_SAFE; [B PR 29](https://github.com/codefoundry-io/triad-codex-dispatch/pull/29). Fresh RED/GREEN, 47 focused /1128 macOS /1126 Ubuntu plus 2 skips; original JSON and both reserved aliases covered. [Spike](../spikes/2026-09-20-b-original-json.md). |
| claude-01, codex-01 | P3b: bind all prepared-review conditions into the digest | CLOSED in source `7a2fdf3ed65aaa008a70c5bfecd2d0b824834216`, round `triad-b-p3b-r2` all four SAFE and ADMITTED_SAFE; [B PR 30](https://github.com/codefoundry-io/triad-codex-dispatch/pull/30). Fresh RED/GREEN, 22 focused /1150 macOS /1148 Ubuntu plus 2 skips; condition axes, both toolkit-byte routes and policy receipt producer/render/dispatch covered. [Spike](../spikes/2026-09-20-b-review-conditions.md). |
| codex-10 | P4: process-cwd relative path resolution | OPEN; resolve D-B2 full-evidence/redaction boundary before affected custody work. |
| claude-04, google-03, codex-07 | P5: Gemini REVIEW policy bytes and shape | OPEN, D-B1 unresolved. Do not weaken B's current catch-all/search guards merely to accept different bytes. V1-V5 remain NOT RUN. |
| claude-05, codex-06, codex-08 | P5: REVIEW no-web across renderers and both AGY paths | CLOSED in source `900ddc5`, complete corrected round `triad-b-p5-web-r2` all four SAFE, ADMITTED_SAFE; [B PR 32](https://github.com/codefoundry-io/triad-codex-dispatch/pull/32). Fresh RED/GREEN, 101 focused /1194 macOS /1192 Ubuntu plus 2 skips; exact custody export/cleanup. Raw INVESTIGATION and dormant-hook boundary preserved. This does not close D-B1/Gemini policy adoption or C29. [Spike](../spikes/2026-09-20-b-review-no-web.md). |
| codex-11 | P5: explicit authorized web-investigation trigger, clause-last and sent-prompt custody | OPEN, D-B2 unresolved for full prompt custody versus hardened audit redaction. |
| claude-09 | Correct inaccurate raw-Gemini readonly wording in units mapping | Documentation correction recorded in local shared commit d7ef763; not a runtime change or global approval. |
| codex-09 | C16 CLI floor and C27 observed-version custody | CLOSED in source `5e8b9fba195b3b5134690f7578c9e0635d206543`, full round `triad-b-c16-r1` all four SAFE, ADMITTED_SAFE; [B PR 31](https://github.com/codefoundry-io/triad-codex-dispatch/pull/31). Fresh RED/GREEN, 23 focused /1173 macOS /1171 Ubuntu plus 2 skips. Version, help, receipt and digest checks preserved. Runtime auth and V1–V5 are not implied. [Spike](../spikes/2026-09-20-b-gemini-version.md). |
| codex-12 | Shared v2 roster/wire/receipt dependent orchestration | DEFERRED per agreed schema boundary, not SAFE or implemented. Any independent rev1 sub-obligation remains mapped in the full case audit. |
| claude-07 | Rejected requested extra render-time fingerprint recomputation | Current capture plus final-integrity workflow intentionally supplies the fingerprint. Preserve that protocol; final review may challenge the evidence. |
| google-04 | Rejected clearing the whole child environment | C11/C25 preserve PATH/auth continuity with route-specific scrubbing; no approval for an empty environment. Final review may challenge the evidence. |

Claude and Codex also carry the same D-B1 policy-byte open question. These are
not additional numbered findings and remain unresolved independently of P1.
The proposed unbounded reader join and a downgrade of reader errors based solely
on AGY extraction are rejected: bounded custody is required and a complete AGY
stdout plus corrupt stderr reproduction demonstrated false success.

At every B change, refresh A commit/path/line comparisons in the relevant spike.
A remains read-only until the owner-designated handoff. Shared authoring records
are local until the owner authorizes publication; installed revision adoption,
host merging and deployment are separate claims.
