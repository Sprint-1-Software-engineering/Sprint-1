# Sprint 1 submission status

Foundation: [PR #43](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/43), approved and merged into `develop`

Main release candidate: [PR #48](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/48), awaiting review

Repository: https://github.com/Sprint-1-Software-engineering/Sprint-1

This is a review package, not a declaration that every submission condition is complete.

## Basis

- SENG 321 Revised Assignment Sprint 1 Project Foundation: pages 2, 4, 11 and 13-17.
- The latest supplied assistant announcement: six deliverables, ZIP plus repository link, evaluator access and individual contribution evidence.
- The separate Examples file has not been supplied. No example-specific requirement is assumed.

## Documents

| Requirement | Artifact | State |
|---|---|---|
| Proposal: problem, stakeholders, outcome, feasibility, scope, license | [Proposal](Project-Proposal-and-System-Vision.md) | Prepared for team review; tutor-specific evidence still pending |
| Vision, responsibilities, exclusions, assumptions and context diagram | [Vision](Project-Proposal-and-System-Vision.md), [diagram](diagrams/system-boundary.svg) | Prepared for review |
| Valid API contract with resources, operations, schemas and errors | [OpenAPI](Openapi.yaml) | 16 operations; validation recorded separately |
| Product, process, architecture, quality, DevOps and implementation owners | [RACI](Team-Members-and-RACI.md) | Named plan; team review pending |
| Git-Flow, Issues, reviews and protected integration branches | [Workflow](Git-Flow-Workflow.md) | Active protection verified on both main and develop; PR and passing check required |
| Prioritized Epic/Feature/Story/Task backlog | [Backlog](Initial-Product-Backlog.md) | Linked GitHub records; implementation remains planned |
| Individual evidence for every student | [Contributions](../CONTRIBUTIONS.md) | Actual links recorded for two accounts; four members have review tasks #44-47 and still need evidence |

## Final gates

- [ ] Record real teacher/student findings and review the scope against them. See [Problem Validation](Problem-Validation.md).
- [ ] All six members confirm roles and estimates, and provide real individual work links.
- [x] Public access permits team members to contribute through forks. Each member must still provide actual work from their own account.
- [ ] Give `mhmttemin` and `goksuyldrm` access; confirm accepted invitations. An organization repository needs at least Read.
- [x] Repository is public; PR, one teammate approval and `Sprint 1 checks` are enforced on both `main` and `develop`, including for administrators.
- [x] Pass local and GitHub checks on the prepared foundation. Recheck after later changes.
- [x] Foundation PR #43 was approved by `mehmetalidmrcgl-hue` and merged into `develop`. Later changes require their own review.
- [ ] Review and merge the assessed version from `develop` into `main`.
- [ ] Create the release tag `v0.1.0-sprint1` on that assessed `main` commit. The name is our convention, not a prescribed course tag.
- [ ] Build the final ZIP from that tagged version; open and check it.
- [ ] One member submits the ZIP in Teams and places the accessible repository URL in the submission description.

## Access audit

The repository is public. Existing collaborator roles remain unchanged: `toprakdaldal` and `mehmetalidmrcgl-hue` have Admin; `kbilgisicok` has Read. No pending invitations were returned. Other team members can use forks. Explicit evaluator invitations remain pending because the owner asked not to change access.

Public visibility and branch protections were explicitly authorized and completed. It does not count as sending or accepting evaluator invitations. The team must confirm that the announcement’s named-account access requirement is met before closing that gate.

## Release notes

See [Release Notes](Release-Notes.md). The review ZIP is for checking content. It must not be described as the final assessed release while these gates remain open.

Each successful CI run publishes `sprint1-review-documents` as an artifact. It contains a ZIP made from that run's commit. The final Teams ZIP must instead match the assessed, tagged `main` version.
