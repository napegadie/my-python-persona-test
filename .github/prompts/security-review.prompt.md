---
mode: ask
description: Review the current changes as a security reviewer
---

Review the current repository changes as a security reviewer.

Focus on:
- unsafe input handling
- overly broad exception handling
- information leakage in errors
- insecure coding patterns
- missing negative tests

Files to inspect:
- calculator.py
- test_calculator.py

Output sections:
1. Summary
2. Must-fix
3. Should-fix
4. Suggested tests
