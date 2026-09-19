# contracts/ — machine-readable contracts

| File | Status (current draft) | Consumers |
|---|---|---|
| `gemini-readonly.toml` | D-9 RULED 2026-09-19 (owner): review legs have no web tools — explicit `google_web_search` / `web_fetch` deny rows at 200 (before: search inherited from the default tier, `--policy` replaces only the user tier — `packages/core/src/policy/config.ts` at v0.46.0 / v0.60.0). The FILE is the contract, vendored byte-for-byte — one definition of equality (A test t50 checks byte identity; host notes live outside the payload); applied without a live run | A `gemini_wrapper.py` attaches it on the read-only posture; B drops the two web tools from its 999 allow list (`bin/policies/gemini-formal-readonly.toml:12-13`) |
| `gemini-readonly.verify.toml` | Verification procedure and evidence requirements for V1–V5; all runtime checks NOT RUN. It distinguishes attempted calls from authoritative pre-dispatch exclusion, canonical tool visibility from alias matching, and compatibility from catch-all effectiveness. See the manifest for the fixture, exact direct-CLI command and attribution rules | the owner, where gemini is in service; results → `decisions/owner-register.md` + C15 test column |
| `exit-tokens.json` | seed = host A's 18-token map as data; B delta noted inside | both hosts' `_common.py` tables, membership-tested (D-11) |
| `review-legs.example.json` | post-cut roster example (owner Q-M/Q-O; codex High #1) | both loaders; schema file to follow |
| `leg-verdict.schema.json` | NOT YET — round r2 (all three families) converged on a superset v2 wire; the mapping and proposed shape are in `leg-verdict-mapping.md`; the schema file follows codex's co-review | both validators; prompt shape pins |
| `leg-verdict-mapping.md` | round r2 output: A↔B mapping table, losses per direction, the proposed v2 shape, the three release properties that must survive | both maintainers (D-3) |
| `review-legs.schema.json` | NOT YET — written from the example once codex confirms the per-vendor blocks | both loaders |
| `receipt-fields.json` | NOT YET — transport receipt vocabulary (`stdin_delivery` class, route/version fields) | both `_common.py` |

Remaining proposals for `gemini-readonly.toml` land only after the manifest checks pass: a canonical `grep_search` allow
row for tool visibility (V3), and a `*` deny below the allows (V5). The exact adoption candidate must pass both read
compatibility and a discriminating deny control; model prose never proves a policy outcome. Effective source-derived
postures at v0.60.0: A has explicit web denies; B allows both web tools at user priority 999 with a `*` deny at 998 until
it adopts D-9. These are source observations, not live conformance results.
