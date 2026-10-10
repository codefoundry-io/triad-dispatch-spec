# B: DL-101 measured network-error carrier

2026-10-10; main3afc4d7, B632f426 plus candidate; read-only A bc8a8a74.
This implements the existing vendor-failure-lines.json row and R-CLASSIFY/C43.

Evidence: the frozen row identifies the network sentence in an ERROR result,
empty response and raw exit1. DL-101 identifies result.error. Current B's
antigravity_wrapper.py:350-368 passes only stderr/status to classify and adds
the terminal error only to diagnostics afterward. Current A's wrapper:135-165
passes typed signals, and _common.py:156 includes the network phrase.

B will pass its parsed result to the existing classifier through an optional
internal argument and recognize this row at the server-capacity rung. It will
not feed all terminal errors into broad phrase matching. Preserve auth STOP,
host timeout, transport failures, strong vendor exit maps, subscription-cap
priority, captured output and diagnostics. No A change or native-leg change.

C43 examples before host code:
- ERROR, response exactly empty, raw1, string result.error containing
  `network issue connecting to the server` on AGY -> server-capacity/64,
  answer withheld; raw stream and exit retained.
- Same phrase in response, tool output, stderr alone, another CLI, an error
  object, another status/exit or a nonempty response does not gain this match.
- Original authentication, host timeout, transport failure, a strong learned
  vendor map or an earlier subscription-cap match keeps its precedence.
- A credits sentence in result.error alone remains unclassified here: its
  runtime carrier is still unmeasured. Stored-record replay uses the wrapper's
  interpreter and must agree without invoking a provider.

Verification plan: tests/test_agy_network_carrier.py plus the affected/full
B suites, fresh dedicated RED/GREEN, four source validators and independent
four-family review. Constructed inputs exercise the recorded contract; no
new vendor failure is claimed. Implementation and verification pending.
