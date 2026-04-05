When reviewing pull requests in this repository:

Focus on three review lenses:

## QA
- Identify missing unit tests and edge-case coverage
- Flag divide-by-zero cases, invalid input handling, and unknown-operation paths
- Recommend exact tests to add

## SRE
- Flag broad exception handling
- Call out weak logging, weak observability, and poor failure behavior
- Highlight operational and supportability risks

## Security
- Flag unsafe input handling
- Flag error messages that expose internal details
- Identify insecure defaults or weak validation

Output format:
1. Must fix
2. Recommended improvements
3. Suggested tests
