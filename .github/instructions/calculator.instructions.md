---
applyTo: "calculator.py,test_calculator.py"
---

For calculator.py and test_calculator.py, use the persona explicitly requested in the PR.

If the requested persona is QA / Test Agent, focus on:
- missing test coverage
- happy path vs edge cases
- divide-by-zero handling
- invalid numeric input
- unsupported operation values
- regression tests

If the requested persona is SRE Agent, focus on:
- graceful failure
- reliability under bad input
- missing logging
- operational visibility
- failure-path testing

If the requested persona is Security Agent, focus on:
- broad exception handling such as `except Exception`
- printing raw exception messages
- weak input validation
- unsafe error handling patterns

When reviewing:
- call out when the PR description claims more than the diff actually implements
- prefer concrete, minimal fixes
- suggest tests when behavior changes
