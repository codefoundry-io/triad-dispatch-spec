# DL-91 — B retired task engine disposition

Shared main fetched at3afc4d7e931e55d601dd74877bdbe65e610a8e59, 2026-10-10.
DL-91 already authorizes removing task/fanout tokens and exits while retaining
Claude permission-denial task-blocked65. This note implements that settled rule;
it introduces no new token, interface, provider behavior or native-leg policy.

B632f426 plus the current candidate still carries fanout-spawn-error in its
classifier, repair registries and replay promotion. Its phrases can still emit
the retired token, so not every deletion is unreachable code. Remove those
memberships and exits68/69. The existing generic unknown result remains for a
failure with no supported diagnosis; do not invent a replacement error class.
Old extension pattern lists for retired fanout are ignored, and new proposals
for that retired class are refused. Valid entries remain effective.

B's production run_cli_with_retry callers are Claude and Gemini wrappers.
There is no B Codex CLI wrapper; native Codex dispatch is independent. Source,
test and script reference inspection finds no consumer of extract_codex_fanout
or extract_implementer_status and only the unused Codex retry arm calls
extract_codex_answer. Remove those extractors/status regex and that arm. Keep
the generic retry callable's parameters, existing wrappers, Claude task-blocked65,
shared locking and historical report-directory cleanup unchanged.

Read-only A3bb4f284 has already removed fanout support. Its active Codex CLI
answer extractor remains, correctly for that host. No A code change is requested;
please flag a concrete B consumer missed by this disposition. A runtime is NOT RUN.

B will refresh its C8 test fixture from exact shared-main token-table bytes,
with the original fixture preserved in pre-unit evidence. That is not whole
shared-revision adoption. Before code, fresh RED will show retired phrase/proposal
behavior and table membership; GREEN covers existing Claude permission denial,
classifier/wrapper/replay behavior, full regressions and four source validators.
No synthetic vendor incident, provider inference or prompt wording change is needed.
