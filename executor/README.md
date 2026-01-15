# Arbitrage Executor

This executor is stateless.

It does not:
- learn
- optimize
- adapt
- retry
- report outcomes

Each run is isolated.

Execution is allowed only if asymmetry exists.
Otherwise, the process exits silently.
