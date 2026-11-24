# Sprint 2 release candidate

Base: main. Head: develop. Keep the release PR draft until final-preparation Issue #83 is reviewed and integrated and evaluator/Figma access is confirmed. Proposed version v0.2.0-sprint2 is not yet created. Do not move existing tags.

## Included work

- Requirements/backlog: PR #62.
- Auth/profile and corrections: #58, #79.
- Editable Figma, flows and exports: #67, #69.
- C4/UML architecture: #70.
- Quality measures, API tests, browser observations and re-tests: #73, #77, #80.
- CI/environment and dated evidence: #64, #78.
- Process and cross-artifact traceability: #82.
- Final terminology, runbook, product decisions and submission overview: [PR #87](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/87); integrate the reviewed preparation PR before ready-for-review.

See [Submission-Overview.md](Submission-Overview.md), [Verification-Report.md](Verification-Report.md) and [Submission-Checklist.md](Submission-Checklist.md). Candidate checks passed locally: 42 automated tests, 17 isolated environment/validation probes, structural release-ready, OpenAPI and whitespace checks. Check exact release-commit CI and peer review before merge. Current local results are not full MVP or hosted acceptance.

Remaining user/admin action: accepted evaluator access for goksuyldrm and nedima68; confirm actual Figma reviewer access. No security settings were changed. Remaining runtime and production decisions are explicitly recorded, not silently marked done. A real usability session and code coverage were not measured.

After approval and release merge: fetch main, create unused v0.2.0-sprint2 on the reviewed final main SHA, build/verify the matching local package and submit through Teams with repository/tag/artifact links. No public ZIP asset upload.
