# Repair research: source evidence and common-host handoff

2026-10-09. Remote main fetched before authoring:
`3afc4d7e931e55d601dd74877bdbe65e610a8e59`; PR13 basis `75dc801`.
Owner decision: D-REPAIR-WEB-20261009. Normative location: R-CLASSIFY, C76.

## Current implementation (source only)

A clean source at `c50b1c8b0b7bfc0f66165c6262653925b697cc58`:
- `.claude/agents/{codex,gemini,agy}-wrapper-repair.md:6` exposes only
  `Read, Grep, Glob`; line 11 explicitly excludes network tools.
- Their analysis steps (codex:74, gemini:72, agy:82) state `Network is off`.
  Their operating discipline also says `No web, no guessing`.
- `3rd-Agent/export_assets/distributed-repair-agent.md.tmpl:6,11,75,161`
  repeats the restrictions. `3rd-Agent/export_plugin.py` renders the shipped
  analyzers from this template, so changing only source agents would omit the
  distributed behavior. No A file was edited or A runtime invoked.

B at `632f42633d3a92d6cb27168cd15c4d4debd8558c` plus its preserved candidate:
`docs/references/repair-protocol.md:51-55` prohibits provider or network calls
and requires escalation when local evidence is insufficient. The prohibition is
in the actual native-child prompt, not merely a statement about a tool name.
No B product prompt, native settings or runtime was changed for this spec update.

These are pending implementations of the newly requested common capability,
not evidence that either host already permits web research or that an observed
production failure was caused by these restrictions.

## Maintainer request

A: expose web search/fetch in the three repair analyzers and their distributed
template and reconcile the contradictory instructions. B: allow those research
operations in the repair prompt and use the host's supported native web capability.
Each host owns its spawn/tool mechanism. Reuse the existing proposal/extension
surface, read-only analyzer and deterministic applier; do not add a new vendor
execution, classifier class or routine log audit. DL-104's independent pending
work stays distinct; this change does not certify its implementation.

Verify C76 on each host: a real failure record needing external explanation can
reach search/fetch and retain useful source attribution; sufficient local evidence
needs no search; unrelated public errors cannot generate entries; unavailable or
inconclusive research reports its limit without guessing or running the vendor.
Check source and distributed behavior. Tests may exercise tool-policy decisions
without claiming a fabricated response is a measured vendor failure. Runtime and
host conformance for C76 are NOT RUN on both hosts.

The shared rule is owner-authorized. Review this same spec commit and report
source-backed disagreements or implementation evidence before claiming adoption.

Spec verification: authoring map 1/1 valid; existing shared tests 182 passed;
whitespace check clean. These checks validate the spec repository, not C76 host
behavior. No new vendor-failure fixture or runtime classification was introduced.
