# Sprint 1 submission status

Review branch: `feature/5-sprint1-foundation`  
Review: [PR #43](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/43)  
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
| Git-Flow, Issues, reviews and protected integration branches | [Workflow](Git-Flow-Workflow.md) | Written policy and CI prepared; enforcement blocked by current private/free plan |
| Prioritized Epic/Feature/Story/Task backlog | [Backlog](Initial-Product-Backlog.md) | Linked GitHub records; implementation remains planned |
| Individual evidence for every student | [Contributions](../CONTRIBUTIONS.md) | Actual links recorded for two accounts; four members have review tasks #44-47 and still need evidence |

## Final gates

- [ ] Record real teacher/student findings and review the scope against them. See [Problem Validation](Problem-Validation.md).
- [ ] All six members confirm roles and estimates, and provide real individual work links.
- [ ] Add missing team access; ensure contributors can create branches and PRs.
- [ ] Give `mhmttemin` and `goksuyldrm` access; confirm accepted invitations. An organization repository needs at least Read.
- [ ] Resolve the private/free-plan limitation and enforce PR, one approval and `Sprint 1 checks` on both `main` and `develop`.
- [x] Pass local and GitHub checks on the prepared foundation. Recheck after later changes.
- [ ] Obtain a teammate review of the final PR, then merge into `develop`.
- [ ] Review and merge the assessed version from `develop` into `main`.
- [ ] Create the release tag `v0.1.0-sprint1` on that assessed `main` commit. The name is our convention, not a prescribed course tag.
- [ ] Build the final ZIP from that tagged version; open and check it.
- [ ] One member submits the ZIP in Teams and places the accessible repository URL in the submission description.

## Access audit

The audit found accepted access for `toprakdaldal`, `mehmetalidmrcgl-hue` and `kbilgisicok`. The last account had Read only. No pending repository invitations were returned. The other three team members and both evaluator accounts were not listed.

Adding access, changing visibility or purchasing a plan needs an explicit team decision. Until then, these gates remain open.

## Release notes

See [Release Notes](Release-Notes.md). The review ZIP is for checking content. It must not be described as the final assessed release while these gates remain open.

Each successful CI run publishes `sprint1-review-documents` as an artifact. It contains a ZIP made from that run's commit. The final Teams ZIP must instead match the assessed, tagged `main` version.
