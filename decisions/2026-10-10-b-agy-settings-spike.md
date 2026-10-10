# B AGY settings interaction: bounded U7 evidence

Basis: B ed8b76f plus the unrelated U6a cleanup candidate; `_agy_settings.py`
unchanged. Shared d3a4412; read-only A c2f28ca2 plus its unrelated vendoring-test
edit. This is provider-free characterization, not a new isolation design.

The actual B `agy_settings_guard(_READ_ONLY_DENY)` was run against a synthetic
settings file inside one invocation-owned temporary fixture. Its caller used
project-a as cwd; a separate Python process in project-b read/wrote that same
fixture file while the guard was active. `AGY_SETTINGS_PATH` was overridden
only inside the diagnostic process; no real settings, auth or provider ran.

Observed control: without another writer, guard exit restores the original
bytes exactly. Observed interaction: project-b sees the temporary deny values;
its added fixture key exists before guard exit but is absent afterward, when
the original bytes are restored. This proves the current merge/restore behavior
across two folders. It is not evidence that a real concurrent AGY/Claude call
has lost settings or that A itself writes those files.

Source: B `bin/_agy_settings.py` `_shared_readonly_guard`, `_snapshot`, `_restore`
and `agy_settings_guard`. Evidence: workspace
`_runs/infra/20261010-spec-to-code/u7-state-spike.py` and `.json`; exit0 and exact
fixture `/private/tmp/triad-u7-state.sdqweauu` removed. No host code was edited.

A currently uses its setup-once custom agents and has no settings transaction
in `3rd-Agent/wrappers/antigravity_wrapper.py`; its agent/tool admission remains
A-owned. Its source also records that older AGY advertised tools beyond the
agent's `tools` list, so merely copying agent YAML is not established proof of
B's replacement containment. Native legs and the unused Claude-agent backlog
are unrelated.

U7's next decision must preserve B's existing read-only/web boundary, validate
the supported actual CLI path, and explain legacy/raw migration plus B-owned
stale backup handling. Collect independent diagnosis and Tier1/runtime evidence
before selecting a replacement. A substantive design/containment change returns
to the owner before dependent implementation. U6a proceeds independently; no
new classifier, environment override policy or generic locking framework follows
from this spike. Existing DL-107/112 remain the governing work items.
