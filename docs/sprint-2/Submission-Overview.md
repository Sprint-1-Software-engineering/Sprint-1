# TutorBridge - Sprint 2 submission overview

Course: BM321 / SENG 321. Deadline: 24 November 2026, 23:59 Europe/Istanbul. Status: delivery candidate under Issue #83; final release/tag and named evaluator access pending. Do not submit a DRAFT archive as a tagged final release.

Repository: [Sprint-1](https://github.com/Sprint-1-Software-engineering/Sprint-1).

## Required artifacts

| Group | Files / sources |
| --- | --- |
| Detailed requirements and refined backlog | [SRS](SRS.md), [backlog](../Initial-Product-Backlog.md) |
| Non-functional requirements and measures | [NFR and quality measures](NFR-and-Quality-Measures.md), [review/test plan](Review-and-Test-Plan.md) |
| Figma prototypes and user flows | [UI/UX handoff](UI-UX.md), [frame transitions](ui-ux/Screen-Flows.md), editable Figma and local .fig links in the handoff, three Mermaid/SVG flows |
| Architecture, C4 and UML | [Architecture](Architecture.md), five editable Mermaid sources and readable SVGs in docs/diagrams |
| Team, roles and evidence | [Roster and IDs](../Team-Members-and-RACI.md), [team/process](Team-and-Process.md), [traceability](Traceability.md), [contributions](../../CONTRIBUTIONS.md) |
| Run and verification instructions | [Local setup](Local-Development-and-Delivery.md), [verification](Verification-Report.md), [submission checklist](Submission-Checklist.md) |

## Candidate validation and limits

On 24 November the final-preparation tree passed 42 automated auth/QA/tooling tests, plus 17 isolated environment/validation probes. Structural release-ready and OpenAPI checks passed. No expected-failure marker remains. The package manifest identifies the exact archived commit; local results do not replace exact-commit CI or independent review.

The current implementation covers registration, login and own profile. Invitations, lessons and assignments are specified and prototyped, not implemented. Role-specific runtime entry and the sample dashboard are recorded gaps. Actual Figma prototype paths and headless-browser checks have separate evidence. There is no real usability study, hosted deployment, full MVP acceptance or measured code coverage claim.

Toprak accepted performance/usability/recovery targets as future verification targets and planned security/accessibility work for Sprint 3 (#84-#86). The NFR distinguishes these decisions from achieved measurements.

## Final delivery fields

Before Teams submission, record the actual release tag and main commit in the submission description and verify they match the package manifest. Proposed unused version: v0.2.0-sprint2; this overview does not create that tag. Include the repository URL, team details and artifact links. The supplied Sprint 2 instructions do not explicitly require ZIP; confirm live Teams attachment requirements.

On 24 November Toprak explicitly authorized Read invitations for goksuyldrm and nedima68; both were sent and await acceptance. mhmttemin has Read. Figma source view and prototype launcher were opened in an unsigned-in browser during the final check. Invitation acceptance is still pending; it is not represented as accepted access.
