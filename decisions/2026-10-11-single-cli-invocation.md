# Single external CLI invocation — replacement guidance

Owner approved the recommended next-unit proposal by "진행" on2026-10-11,
after the briefing described removing capacity restarts and schema-correction
calls, the earlier transient recovery loss, and preserved explicit retry.
This is a replacement contract for both hosts, not a request to copy B internals.

## Evidence and current behavior

B25372be `bin/_common.py::run_cli_with_retry` repeats capacity failures up to
two additional calls, sleeping15/45seconds, and can call again after failed
local schema validation. Ordinary/raw Claude and Gemini use it. Claude's native
structured-output path and formal Google already avoid these outer restarts.
Read-only A1de943af `3rd-Agent/wrappers/_common.py::run_cli_with_retry` at2862
has the same common loops; its native Claude spawning remains A-owned.
Shared main was fetched at3afc4d7; draft3061281; PR13 had no newer comment after
6101997909. A's code is evidence of current behavior, not design authority.

## Selected outcome and tradeoff

R-TERMINAL/C78 now return the first capacity/schema failure using existing
64/66 outcomes. Vendor-internal request retries remain the vendor's concern.
No claim is made that every vendor retries every failure. A transient error
previously recovered by another automatic CLI invocation can now surface sooner;
the user/leader diagnoses it and explicitly retries if warranted. Valid output,
auth STOP, known failure classification, exact input and review bindings remain.
Do not add a retry switch, scheduler, error taxonomy, timer or replacement agent.

Preflight probes are not inference calls. Manual failed-entry retry under
R-RETRY remains; a completed review finding is not a provider failure. Native
host legs, model/effort, user settings, AGY profiles and cleanup are outside this
bounded implementation. B preserves its helper signature and zero-valued record
fields for existing consumers while removing the loops; no schema migration.

## Verification and adoption

Before implementation, use real local subprocess fixtures to count launches
and capture exact prompts for capacity, schema-invalid and success controls.
Include auth, transport and formal-path regressions; independently review the
complete change. Local fixtures establish wrapper behavior, not current vendor
conformance. Both hosts record their own implementation/test status in C78.
No host completion, adopted revision, merge, installation or release is claimed.
