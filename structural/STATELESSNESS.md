## Statelessness Constraint

This field must remain stateless.

Forbidden elements:
- databases
- caches
- local storage
- session memory
- execution logs
- performance counters

Allowed elements:
- transient variables
- in-memory comparison during execution
- immediate execution or immediate termination

Statelessness is not an implementation detail.
It is the core integrity condition of this field.
