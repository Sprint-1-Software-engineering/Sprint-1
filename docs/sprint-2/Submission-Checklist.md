# Sprint 2 Submission Checklist

Owner: Osman Berke Özdemir (@makucheez). Tracking: [#63](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/63). DevOps implementation: [PR #64](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/64), independent review pending.
Readiness: **not ready for final submission**. Review date: 19 November 2026. These unchecked items are gates, not claims of completion.

## Source and deadline

The team-supplied copy of the Teams assignment states 24 November 2026, 23:59 Türkiye time (UTC+03:00), weight 20%, and permits multiple submissions. It requires the four groups below plus team/repository, release/tag, owners and artifact links. The assignment copy does not specify ZIP. Live Teams instructions and attachment format have not been accessed in this session; the submitting member must verify them before upload. Do not carry forward the old Sprint 1 ZIP rule automatically.

The supplied BM321 semester rubric places first working MVP and 50% unit-test coverage CI in Sprint 3, and one-command Docker operation in the final submission. Current smoke verification does not establish 50% coverage or full MVP acceptance. Document names below are team proposals, not instructor-mandated names or quotas.

## Four required delivery groups

| Group | Owner / dependency | Current evidence and remaining gate |
|---|---|---|
| Detailed SRS and refined backlog | Toprak | [#59](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/59), [PR #62](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/62); open, awaiting review/integration |
| NFR and quality-measure specification | Berat | Separate artifact not in reviewed develop/PR branches; real methods, thresholds, environment and result status needed |
| Figma prototype and user flows | Kemal with Arda | No Figma file/prototype link or Sprint 2 flow sources found in reviewed trees; actual accessible Figma and flows required |
| C4/UML architecture | Mehmet with Osman's deployment support | Full Architecture.md/C4/UML/schema set not in reviewed trees; [deployment handoff](Deployment-and-Recovery.md) is available but does not satisfy this entire group |

- [ ] Integrate reviewed SRS and backlog; preserve existing Issue identities and resolve scope decisions.
- [ ] Integrate NFR/quality and real test plan/report; distinguish targets, planned tests and observations.
- [ ] Add real Figma file and prototype URLs and verify access as a reviewer; include user flows and readable exports.
- [ ] Integrate C4/UML, database schema, interfaces and architecture decisions; pair diagram exports with editable sources.
- [ ] Resolve Python/Express, opaque-token/JWT and 8000/3000 mismatches with owners; update SRS/OpenAPI/architecture/runbook consistently.

## Team, contributions and review

Repository: [Sprint-1-Software-engineering/Sprint-1](https://github.com/Sprint-1-Software-engineering/Sprint-1).

| Member / GitHub | Sprint 2 responsibility |
|---|---|
| Toprak Daldal / toprakdaldal | Product, SRS and backlog |
| Mehmet Ali Demircioğlu / mehmetalidmrcgl-hue | Architecture, schema, API/code decisions |
| Berat Erdem Yalçın / SunsetEva | Quality, NFR and tests |
| Osman Berke Özdemir / makucheez | Local environment, CI, deployment and delivery |
| Kemal Efe Bilgisiçok / kbilgisicok | Figma and UI/UX |
| Arda Demir / ardmr26 | Process, user flows and traceability |

Student IDs and RACI are in [the team record](../Team-Members-and-RACI.md). Actual authored work/reviews belong in [contributions](../../CONTRIBUTIONS.md).

- [ ] Each member records their own real Issue, commit, PR and review links; assignment alone is not completed-work evidence.
- [ ] Every release-bound PR has another person's review of its latest changes; no self-approval or bypass merge.
- [ ] Mehmet and Berat independently reproduce/check the [local procedure](Local-Development-and-Delivery.md); no teammate run is recorded yet.
- [ ] Review [PR #58](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/58), reconcile its main target with Git-Flow, fix validation/role issues and integrate through the agreed workflow. Do not treat its basic smoke as complete story acceptance.
- [ ] Check Arda's traceability from FR/NFR to Issue, Figma, API, architecture and verification; mark unimplemented runtime work honestly.

## Access and CI gates

19 November API observations using makucheez: both branches report protected; their branch summaries retain required context `Sprint 1 checks`, enforcement `everyone`. Detailed protection endpoints returned 404 with this Write account, and effective rules endpoints returned empty arrays. Exact approval settings could not be independently verified; the administrator must inspect them without weakening them. Historical workflow statements are not a fresh settings audit.

Accepted collaborator listing contains `mhmttemin` with Read; `goksuyldrm` and `nedima68` are absent. This confirms neither a pending invitation nor accepted access for those two accounts. The existing README asks for all three. An administrator must resolve the stated evaluator-access requirement and verify acceptance. No permissions were modified.

- [ ] Preserve required `Sprint 1 checks`, PR/review/conversation requirements and administrator enforcement.
- [ ] Review successful CI logs on the exact integrated/release SHA, not an old feature or reference SHA.
- [ ] Run actual integrated auth/QA tests when present; skipped runtime checks do not establish tested application behavior.
- [ ] Run `python3 scripts/check_sprint2.py --release-ready`; adapt proposed file paths if the team agrees different names. This only checks structural integration, not full release approval.
- [ ] Independently inspect Figma and remote document/diagram access; local-link validation is not permission verification.
- [ ] Ensure no real secrets, student records, SQLite databases, uploads or backups are tracked or packaged.

## Release and package procedure

At this review develop is an ancestor of main with no release content difference; Sprint 2 feature PRs are not integrated. GitHub cannot create a meaningful develop -> main release PR yet. [A concrete draft description](Release-PR-Draft.md) is prepared; do not create an empty placeholder PR or merge features just to make it possible.

- [ ] Integrate team artifacts via independently reviewed feature PRs into develop.
- [ ] Refresh refs and open a **draft** develop -> main release PR with the prepared description and actual evidence. Fill in real Issue/PR/review, Figma and CI links.
- [ ] Run/check the full release candidate; resolve failures and obtain independent latest-push review before merge.
- [ ] Merge through the protected workflow only after all gates; do not push directly to main.
- [ ] Fetch main, identify the final reviewed SHA and choose an unused Sprint 2 tag, proposed `v0.2.0-sprint2`. This tag has not been created.
- [ ] Create a new tag at that final main commit after approval; never move Sprint 1 or existing tags.
- [ ] Run `python3 scripts/build_delivery.py --ref v0.2.0-sprint2 --output-dir /tmp/tutorbridge-delivery` after `git fetch origin main --tags`. The tool requires the tag to equal origin/main and all structural team paths to exist in the tagged tree; manual gates still apply.
- [ ] Open and inspect the resulting ZIP, manifest SHA and file hash; verify its source commit matches the actual assessed tag. A ZIP is a convenient local package, not proof Teams requires it.
- [ ] One member submits through Teams before the deadline, including team/roles, repository, actual tag and real artifact links; verify upload completion.

A preview package is explicitly marked DRAFT and is not a release or completed team submission. Deliver packages through chat/local files. Do not upload ZIPs as public GitHub release assets unless the user separately requests it.
