# contracts/ — machine-readable contracts

| File | Status (rev-0 draft) | Consumers |
|---|---|---|
| `gemini-readonly.toml` | seed = host A's shipped file; header EXPANDED with the version-pinned source cite (A's shipped substance was already right: `--policy` replaces the user tier; admin/workspace/defaults still load — `packages/core/src/policy/config.ts` at tags v0.46.0 and v0.60.0, raw source fetched 2026-09-19) | A `gemini_wrapper.py` attaches it on the read-only posture; B keeps `gemini-formal-readonly.toml` until the rename is specified (codex second pass) |
| `exit-tokens.json` | seed = host A's 18-token map as data; B delta noted inside | both hosts' `_common.py` tables, membership-tested (D-11) |
| `review-legs.example.json` | post-cut roster example (owner Q-M/Q-O; codex High #1) | both loaders; schema file to follow |
| `leg-verdict.schema.json` | NOT YET — waits for the D-3 three-family adjudication (A: 3 verdicts + 4 severities + `context_known`; B: SAFE/NOT-SAFE + 3 + `affected_surfaces_inspected`, `open_questions`); the mapping must be lossless on finding fields too (codex C7) | both validators; prompt shape pins |
| `review-legs.schema.json` | NOT YET — written from the example once codex confirms the per-vendor blocks | both loaders |
| `receipt-fields.json` | NOT YET — transport receipt vocabulary (`stdin_delivery` class, route/version fields) | both `_common.py` |

Proposed changes to `gemini-readonly.toml` (NOT applied to the seed; each becomes a case before it lands): add a
`grep_search` allow row beside `search_file_content` (current registered name per the Gemini CLI tools reference,
2026-09-01); add `toolName = "*"` deny at a priority below the allows so unlisted tools fail closed regardless of
headless defaults; network tools (`google_web_search`, `web_fetch`) follow the D-9 round.
