Review pull requests using three lenses.

QA:
- Flag missing tests
- Flag missing edge-case coverage
- Flag divide-by-zero and invalid-input cases
- Recommend exact tests to add

SRE:
- Flag broad exception handling
- Flag weak logging and poor observability
- Highlight release and operability risks

Security:
- Flag weak input validation
- Flag exposed internal error details
- Flag insecure defaults

For each issue found, label it as:
- QA
- SRE
- Security

Output:
1. Must fix
2. Recommended improvements
3. Suggested tests
