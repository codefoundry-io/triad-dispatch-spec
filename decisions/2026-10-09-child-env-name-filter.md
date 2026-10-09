# Child environment name filtering — U2c

Basis: remote main3afc4d7, PR13 b8512b6; B632f426 plus preserved dirty candidate;
A af54fb82 (comment basis bb933c6b). This implements the existing R-NOCOST/C11/
C17/C37 agreement, not a new authentication design or native-leg mechanism.

Pre-implementation provider-free spike on 2026-10-09 extracted the existing
normative list: 17 loader names, 49 credential/endpoint/model-selector names,
four Google project names. B's ordinary shared helper retained all53 non-loader
names; formal Gemini retained40 forbidden names, formal AGY retained43. These
are synthetic mappings and presence checks, not real credentials or vendor
dispatches. B's Google diagnostics also applies the AGY list to Gemini, dropping
its required project exception. A's literal name sets match all70 agreed names.

Both helpers use `for k, v in src.items()` before filtering. A guarded synthetic
Mapping demonstrates that B retrieves an omitted value before rejecting its
name. A has the same source construct, but its helper was not executed here.
R-AUTH already says the values are never read: C75 makes the testable boundary
explicit before dependent implementation. Iterate names and retrieve only kept
values. This does not inspect or mutate credentials, provider settings or the
parent environment. It makes no billing-route attestation.

B correction: one common full list for every vendor child; route identity selects
only the existing four-name Gemini project exception. Apply it at the shared
spawn and standalone version/help/diagnostic probes. Keep PATH, configuration
pointers and GOOGLE_GENAI_USE_GCA, and preserve explicit extra removal callers.
The proposed interface is scrubbed_child_env(base=None, *, cli=None, remove=()).
No route identity defaults to removing the project group. Synthetic helper and
actual local subprocess tests cover normal/repair/formal consumers and probes,
without calling authenticated CLIs. Dedicated RED/GREEN and the existing review
gate precede any completion claim. No implementation completion is claimed yet.

A request: verify C75 on your helper and change name filtering if needed; keep
the already matching set and Gemini exception. No host-native change requested.
The shared rule remains authoritative; A is supporting source evidence only.

## PR13 maintainer reply 6078141262

The reply agrees with R-AGENT-ROLES/C73 and the AGY profile contract/C72.
Official Claude tools-reference (Glob tool behavior, read 2026-10-09) confirms
that a subagent listing Glob/Grep and omitting Bash regains its listed search
tools. A reports a Claude2.1.289 same-tool-shape probe; this is A-reported runtime
evidence, not rerun by B. B's previously measured null-agent CLI path stays.
https://code.claude.com/docs/en/tools-reference#glob-tool-behavior

A source af54fb82 confirms embedded AGENT_BODIES and check_agent_file's exact-byte
comparison. Its wrapper-digest binding is reported as planned Task6e, and search
event evidence as planned Phase12T4; neither is certified complete here. Keep
tests.A NOT RUN until its named conformance evidence arrives. No extra live
probe or B agent/default change is needed. C74's later request remains pending;
this comment explicitly covers earlier commits through b085a6e, not U2b.
