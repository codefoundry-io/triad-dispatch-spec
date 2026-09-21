# contracts/ — machine-readable contracts

| File | Status (current draft) | Consumers |
|---|---|---|
| `gemini-readonly.toml` | A's unchanged 100/200 profile, including D-9 explicit web denies. Vendored byte-for-byte; host notes stay outside the payload. Applied without a live run | A `gemini_wrapper.py` read-only posture; B selects its separate profile below under D-B1 |
| `gemini-readonly.verify.toml` | Verification procedure and evidence requirements for V1–V5; all runtime checks NOT RUN. It distinguishes attempted calls from authoritative pre-dispatch exclusion, canonical tool visibility from alias matching, and compatibility from catch-all effectiveness. See the manifest for the fixture, exact direct-CLI command and attribution rules | the owner, where gemini is in service; results → `decisions/owner-register.md` + C15 test column |
| `gemini-readonly-b.toml` | D-B1 separate B profile candidate: preserves existing 999/998 controls, canonical search and Plan Mode transition denies; moves both web tools into explicit denies. Byte equality applies to this complete selected profile; A payload is unchanged | B `bin/policies/gemini-formal-readonly.toml`, after explicit candidate integration; no overlay |
| `gemini-readonly-b.verify.toml` | B1–B3 live effects NOT RUN; independent exact policy digest and verification-only Plan Mode command. A V1–V5 remain unchanged | B owner where Gemini is in service; results → C15 B column and owner register |
| `exit-tokens.json` | seed = host A's 18-token map as data; B delta noted inside | both hosts' `_common.py` tables, membership-tested (D-11) |
| `review-legs.example.json` | v2 illustrative roster template; placeholders make it non-runnable until adapter catalog resolution | both loaders; validates against `review-legs.schema.json` |
| `leg-verdict.schema.json` | Draft 2020-12 v2 canonical admission schema; materializes the aligned `leg-verdict-mapping.md` choices; candidate, not tagged/adopted | both validators; v2 prompt shape pins |
| `leg-verdict-mapping.md` | round r2 output: A↔B mapping table, losses per direction, the proposed v2 shape, the three release properties that must survive | both maintainers (D-3) |
| `review-legs.schema.json` | Draft 2020-12 named overrides and `$defs.resolvedRoster`; actual route/model/effort capability checks remain host adapters | both loaders |
| `receipt-fields.json` | Draft 2020-12 common `transport` object for existing audit/run-log envelopes | both `_common.py` and native receipt producers |

Integration and legacy compatibility: [rev-2 implementation specification](../decisions/rev-2-implementation-spec.md).
Host-profile equality and investigation evidence semantics:
[D-B1/D-B2 amendment](../decisions/2026-09-20-host-policy-and-evidence-amendment.md).
Authoring validation uses `python3 -m pytest -q tests` with `requirements-dev.txt`; the suite exercises canonical
schema validity and boundary examples. It proves neither host adoption nor authenticated CLI behavior. Duplicate
JSON members must be rejected at the original-text boundary before schema validation; invocation binding and actual
adapter capabilities are checked separately. No remote schema resolution or custom validation engine is required.

Remaining proposals for `gemini-readonly.toml` land only after the manifest checks pass: a canonical `grep_search` allow
row for tool visibility (V3), and a `*` deny below the allows (V5). The exact adoption candidate must pass both read
compatibility and a discriminating deny control; model prose never proves a policy outcome. Effective source-derived
postures at v0.60.0: A has explicit web denies; B allows both web tools at user priority 999 with a `*` deny at 998 until
it adopts D-9. These are source observations, not live conformance results.
