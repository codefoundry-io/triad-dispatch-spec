# B typed classifier-extension loader — DL-97 / DL-106

Remote main verified at3afc4d7e931e55d601dd74877bdbe65e610a8e59. Current B632f426
plus candidate `_load_classifier_extension` keeps every string exit-map value,
which allows a hand edit to emit an unsupported token or a wrapper-only class.
DL-97/R-CLASSIFY already requires those entries to be ignored with one log line.
DL-106 requires dropping an extension's exit0 key. C77 makes those existing
rules directly testable before B's correction.

Read-only A c890731 plus its concurrent dirty `_common.py` uses the existing
VENDOR_EXIT_PROPOSAL_CLASSES set and drops nonpositive numeric keys at load
(3rd-Agent/wrappers/_common.py:1073-1093). A source is reference evidence; no
claim is made that B ran A's suite or that A's pending work is complete.

B's bounded correction uses its own existing vendor-exit class set, drops
zero-valued keys using the same integer interpretation as classify, and logs
each rejected entry. It preserves valid siblings and the source file bytes.
R-CLASSIFY's separate new-auth-proposal refusal does not remove existing curated
entries: the loader's supported class set retains oauth-env, while the applier
still refuses every new oauth-env proposal. No new classifier vocabulary,
provider call, native mechanism, key-range policy or shared file migration.

The pre-existing B AGY weak fallback is reachable; its removal is not part of
this loader correction. Other DL-106 removal candidates require their own
reachability evidence. Please check C77 against A's corresponding loader and
report only an actual contract disagreement or missing outcome. B implements
the settled common behavior; no A internal code is requested as a port.

Verification: local temporary extension fixtures exercise unsupported tokens,
wrapper-only classes, zero spellings, supported siblings/curated authentication,
ordinary classification, and file immutability. No vendor incident is inferred
from these operator-edit fixtures. B RED/GREEN and review evidence pending.
