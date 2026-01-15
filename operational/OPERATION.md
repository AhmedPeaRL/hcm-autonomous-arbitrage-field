# Operational Layer

This field does not operate continuously.
It does not seek opportunities.

Execution is allowed only under blind triggering.

Permitted triggers:
- fixed-time triggers (cron without feedback)
- external signal triggers (price feed webhook)

Execution rules:
- one trigger → one execution
- no retries
- no adjustment of frequency
- no reaction to outcomes

If execution fails, it fails silently.
If execution succeeds, it leaves no trace.
