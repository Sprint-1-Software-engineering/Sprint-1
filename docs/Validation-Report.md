# Validation report

Date: 5 November 2026.

## Local checks

Command: `python scripts/check_submission.py`

Result: PASS.

- OpenAPI 3.0.3 contract is valid.
- 16 operations have unique operation IDs.
- 27 model and error examples match their schemas.
- The main booking journey includes success, input errors and conflict responses.
- Every API operation referenced by a backlog story exists in the contract.
- Required document links resolve locally.
- The boundary diagram is well-formed SVG.
- Each RACI row has one accountable owner and at least one responsible member.
- `git diff --check` found no whitespace errors.

Versions: openapi-spec-validator 0.7.2, PyYAML 6.0.3. Dependencies are pinned in `requirements-docs.txt`.

## GitHub check

The workflow uses the same validator. Its check name is `Sprint 1 checks`.

[Current workflow runs](https://github.com/Sprint-1-Software-engineering/Sprint-1/actions?query=branch%3Afeature%2F5-sprint1-foundation)

## Limits

These checks validate the design artifacts. They do not test a running application, confirm interviews or individual work, grant access, enforce branch rules, replace teammate review, or create the final release.
