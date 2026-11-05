# Git-Flow workflow

## Branches

- `main`: assessed releases. Each Sprint submission gets a tag here.
- `develop`: integrates completed work for the next release.
- `feature/<issue>-<short-name>`: one Issue or small task, created from current `develop`.
- `release/*` and `hotfix/*` are optional. We will create them only when needed.

## Change process

1. Open an Issue with purpose, owner, acceptance criteria and dependencies.
2. Update from `develop` and create a short feature branch.
3. Make meaningful commits using your own account. Reference the Issue.
4. Open a PR into `develop`. Link the Issue and include validation evidence.
5. A teammate reviews the change. Resolve feedback and rerun checks.
6. Merge after at least one valid approval and passing required checks.
7. For a submission, review a PR from `develop` to `main`.
8. Tag the assessed `main` commit, prepare the ZIP and update submission links.

Use a merge commit when integrating release history. Preserve authorship. Do not force-push shared integration branches. Keep Issues open until their actual criteria are met. Closing keywords may not close an Issue when the target is not the default branch; check its state.

## Required rules for main and develop

- Require a PR and one approving teammate review.
- Dismiss stale approvals when new commits change the diff.
- Require the `Sprint 1 checks` status check.
- Resolve review conversations.
- Apply rules to administrators as well.
- Block force pushes and branch deletion.

The automation validates the OpenAPI contract, examples and required submission files. It does not prove that the application works.

## Current limitation

The organization currently uses GitHub Free with a private repository. GitHub reports that branch protections are not enforced on this plan. Written rules alone do not satisfy the enforced-workflow requirement.

The team must choose a supported private-repository plan or explicitly agree to make the repository public. A course-approved exception would need to be documented. Visibility and access will not be changed silently.

## Traceability and past work

Link Issues, commits, PRs, diagrams and the release in [CONTRIBUTIONS.md](../CONTRIBUTIONS.md) and [Submission](Submission.md). Earlier direct commits remain in history. They are not re-labelled as reviewed PR work.

PR #2 was merged from `main` into `develop`. The API returned no submitted reviews for that PR at the audit. A merge alone is not evidence of a review. Current PRs must use the review process above.
