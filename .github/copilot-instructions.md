Review pull requests using three lenses.

Prefix every finding with exactly one label:
[QA], [SRE], or [Security]

QA:
- missing tests
- edge cases
- regressions
- correctness

SRE:
- broad exception handling
- weak logging/observability
- operability and supportability risks

Security:
- unsafe input handling
- exposed internal error details
- hardcoded secrets
- insecure defaults

Prefer concrete findings tied to the changed code.
3. Suggested tests
