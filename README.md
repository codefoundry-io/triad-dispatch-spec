# triad-dispatch-spec — shared specification for the TRIAD dispatch hosts (rev-0 draft, 2026-09-19)

Shared specification for the two TRIAD dispatch hosts: the Claude-hosted `triad-dispatch` (source of truth `~/triad`) and
the Codex-hosted `triad-codex-dispatch`. Owner-designated home (2026-09-19): this repository, public, owner-only push. rev-0 is a DRAFT pushed at the owner's
instruction ("그 레파지토리 자체가 제작소 역할을 할테니까"): the repository is the workshop — codex reviews and amends in place,
revisions follow; nothing here authorizes implementation on either host (owner Q-F).

**What this repository is (owner Q-V, verbatim):** "UI 요소가 없는 실험적 시도로 컨셉만 잡아서 Likec4 없이 스펙저장소를
가벼운 실험소처럼 쓰자" — a lightweight experiment lab for writing specs and accumulating behavioral cases. Concept level.
No UI, no LikeC4, no generated documentation, no cross-host release federation. Both hosts stay independently owned and
released; each host records the revision of this repository it conforms to.

## Layout

```
triad-dispatch-spec/
├── README.md                      this file: purpose, layout, how a host adopts a revision
├── AGENTS.md                      pointer-only entry (byte-identical to CLAUDE.md)
├── CLAUDE.md                      pointer-only entry (byte-identical to AGENTS.md)
├── reference/                     common guidance, written ONCE — every host doc points here
│   ├── README.md                  index + the one-source-per-fact table
│   ├── spec-authoring.md          HOW specs are written in this lab (the method)
│   ├── review-rules.md            agreement, correction re-review, roster, Google leg, smell criterion, containment, no-cost
│   └── process.md                 the shared flow (one diagram) + the failure-diagnosis rules
├── prompts/                       review prompt text — the ONE editable copy (owner Q-U); hosts vendor at the adopted revision
├── contracts/                     machine-readable contracts (schemas, token tables, policy files)
├── cases/cases.json               behavioral cases with stable ids — the accumulating test asset
├── units.json                     surface → common shipped name → contract → preserved host exceptions → host paths
├── decisions/owner-register.md    owner rulings and their effect (site-neutral; verbatim record stays in the host plan)
└── CHANGELOG.md                   one entry per revision
```

## How a host uses a revision

1. A revision is a git tag `rev-N` on `main`. The owner tags it after the other leader has read the handed folder and its `CHANGELOG.md` entry (owner Q-T); no signature ceremony.
2. Each host repository records the revision it conforms to in one file (`SPEC_REVISION`, one line: `rev-N` + the tag's commit). The host vendors `reference/`, `prompts/*.md` and the `contracts/` files it consumes at that revision with the payload bytes UNCHANGED, recording revision and source digest in an adjacent small manifest (never inside the file — JSON has no comment syntax and byte equality is the check), so the adopted rules are available offline at the pinned revision; a live main-branch URL never changes installed behavior. It runs the `cases/` its `units.json` row maps to its own tests.
3. A host may lag a revision. Drift BETWEEN hosts is a REPORT (which revision each conforms to), not a release block (owner Q-P settled the location, not the enforcement mode). A host's failed required check against the revision it ITSELF claims is a local defect of that host.
4. Authoring vs publication: either leader AUTHORS amendments here (a folder mirroring this layout, read by the other leader); only the OWNER publishes — pushes and tags. A review request or an attached maintainer instruction is never blanket authority to push or tag. Decisions that need the owner are asked in advance; the ruling and its effect land in `decisions/owner-register.md`.

## Reading order

`reference/README.md` → `reference/review-rules.md` → `reference/process.md` → `reference/spec-authoring.md` → `prompts/`
→ `contracts/` → `cases/` + `units.json` → `decisions/`.
