# Sprint 2 team and process

Updated: 24 November 2026. Process record owner: Toprak Daldal (@toprakdaldal). Tracking: [#81](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/81). Source baseline: develop at `1897f24` (PR #80 integrated).

## Team and responsibility

Names, student IDs and GitHub accounts are in the [team roster](../Team-Members-and-RACI.md). Actual authored work and reviews are in [CONTRIBUTIONS.md](../../CONTRIBUTIONS.md). Role assignment is not proof of completion.

Toprak has taken responsibility for the remaining Sprint 2 process and traceability documents. This handover does not reassign future product implementation Issues or rewrite previous work. The original team roster remains intact.

| Work | Responsible / accountable owner | Input or review needed | Evidence |
| --- | --- | --- | --- |
| SRS and backlog | Toprak | Technical input from Mehmet; quality input from Berat | [PR #62](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/62) |
| Architecture and API alignment | Mehmet | Toprak for scope; Berke for deployment | [PR #58](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/58), [PR #70](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/70) |
| Figma and user flows | Kemal; Toprak authored the completion | Berat for quality checks | [PR #67](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/67), [PR #69](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/69) |
| NFR and test plan | Berat | Toprak for targets; Mehmet for technical decisions | [PR #73](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/73), [PR #77](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/77), [PR #80](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/80) |
| CI and delivery evidence | Berke | Mehmet / another teammate for review | [PR #64](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/64), [PR #78](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/78) |
| Process, cross-artifact traceability and submission coordination | Toprak | Independent teammate review of this change | [#81](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/81) |

The owner does the work and owns the result; named input/review roles are requests, not invented approvals. Each release-bound PR needs one actual teammate approval of the latest push. Toprak cannot approve this process-documentation PR.

## Backlog and working order

The [backlog](../Initial-Product-Backlog.md) preserves 3 epics, 6 features, 15 stories and 15 tasks. Initial estimates are 45 story points and 64 task hours; those are different units and are not added together. They are planning estimates, not actual effort or an approved Sprint 2 capacity commitment.

Identity precedes connections; connections and availability precede requests; approval/cancellation and file access follow their prerequisites. Existing Issue assignees remain the implementation assignments. The [traceability matrix](Traceability.md) links their acceptance criteria to design and verification.

Before starting a task, check its owner, acceptance criteria, priority, estimate, dependencies and affected contract. New behavior or uncertain expected results go into an explicit decision before implementation. Do not close an implementation story merely because its documentation is ready.

## Workflow and definition of done

1. Track a focused task in an Issue. Create a feature branch from current develop.
2. Commit through the actual contributor's account. Keep meaningful changes and existing history.
3. Open a develop-targeted PR with scope, linked Issues, checks and known limits.
4. A teammate reviews the latest change. New pushes need fresh approval where protection dismisses the old one. Resolve feedback and pass required checks; do not bypass rules.
5. Merge reviewed work into develop. Update the relevant contribution and verification records.
6. After final checks and decisions, review a develop-to-main release PR and tag the final main commit. Never move Sprint 1 tags.

For documentation, done means requirements and artifact links agree, sources and readable diagrams are present, checks pass and a teammate has reviewed the final change. For implementation, the relevant acceptance criteria must also pass. Prototype navigation is not backend authorization or full product acceptance. See [Git-Flow](../Git-Flow-Workflow.md) for the repository rules.

## Integration and evidence

| Change | State at this baseline | Verification boundary |
| --- | --- | --- |
| #62 requirements | Merged | SRS/backlog preparation; does not accept all stories |
| #58 and #79 auth | Merged | Registration, login and own-profile API; malformed-header fix and login wording correction |
| #69 Figma | Merged | Shared editable source, flows and representative prototype clicks; no backend result |
| #70 architecture | Merged | C4/UML proposal and sources; hosting/production decisions remain open |
| #73, #77 and #80 quality | Merged | API test plan/results, headless-browser findings, CI references; no user-study or coverage result |
| #78 delivery evidence | Merged | Updated CI label and dated submission/verification records |

The [quality report](Review-and-Test-Plan.md) records 42 passing automated tests at `7fccc47`, including 23 QA cases, with no expected failures after #79. Its CI link is [run 45250755596](https://github.com/Sprint-1-Software-engineering/Sprint-1/actions/runs/45250755596). Historical failures remain dated; they are not current results. Headless-browser findings include missing role routing and error announcements. No stakeholder usability session or measured code coverage is claimed.

## Decisions and remaining work

| Item | Decision / action owner | Current disposition |
| --- | --- | --- |
| Quality thresholds and validation sample | Toprak with Mehmet / Kemal as listed in the NFR | Still Proposed; review [NFR section 7](NFR-and-Quality-Measures.md) |
| Input errors, static asset serving and login throttling | Mehmet with Toprak for scope | [#75](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/75); proposals, not implemented requirements |
| Teacher/student runtime entry | Mehmet, Toprak | [#61](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/61); headless checks show both roles reach the sample student dashboard |
| Figma naming and clarity | Kemal / Toprak | [#76](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/76); shared loading visuals are intentional, clarity suggestions remain |
| Backend, tokens, hosting, recovery and dataset growth | Owners listed in SRS OD-01 to OD-07 | Record decisions or explicit deferrals; do not invent approval |
| Contract/design inconsistencies | Mehmet with Toprak | See the open consistency notes in Traceability.md |

## Submission handoff

Deadline: 24 November 2026, 23:59 Europe/Istanbul. The supplied Sprint 2 Teams instructions require SRS/backlog, NFR/quality measures, Figma/user flows and C4/UML architecture, plus team responsibilities, repository, release/tag and artifact links. The Sprint 2 text does not explicitly require ZIP; verify the live attachment instructions. A local ZIP may be prepared for convenience.

Berke prepares the final evidence/package after integration. Toprak checks scope and submits through Teams. Keep source design access, real contribution/review links, the final tag and exact-commit CI evidence. Follow the [submission checklist](Submission-Checklist.md). This process record creates no release/tag, grants no access and claims no completed submission.
