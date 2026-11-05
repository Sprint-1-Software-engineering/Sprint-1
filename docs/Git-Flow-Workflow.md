# Repository Workflow and Git-Flow

Repository: https://github.com/Sprint-1-Software-engineering/Sprint-1

## Branches

- `main`: reviewed release snapshots. Each Sprint submission gets a tag here.
- `develop`: integrates completed work for the next release.
- `feature/<issue>-<name>`: a short branch from current `develop` for one Issue.
- `release/*` and `hotfix/*`: optional; create them only when needed.

## Working rules

1. Open an Issue with purpose, owner, acceptance criteria, estimate and dependencies.
2. Create a feature branch and commit meaningful work from your own account.
3. Open a PR into `develop`. Link the Issue and actual validation evidence.
4. A teammate reviews the change. Resolve feedback and pass `Sprint 1 checks`.
5. Merge the reviewed work. For submission, review a PR from `develop` to `main`.
6. Tag that main commit and build the matching ZIP. Do not move an existing release tag after changes.

Both `main` and `develop` enforce PRs, one approving review and passing checks. Administrators follow these rules too. New changes dismiss stale approvals. The latest push needs another person's approval. Resolve conversations; force pushes and branch deletion are blocked.

Members without Write access can use a fork and open a PR into `develop`. Keep authorship and dates accurate. Earlier direct commits remain visible in history; do not describe them as reviewed PR work.

## Evidence

Use [CONTRIBUTIONS.md](../CONTRIBUTIONS.md) for each member's actual Issue, PR, commit and review links. The validator checks the API and document structure, not runtime behavior or interviews. GitHub keeps the check logs. ZIP delivery is handled separately.

Existing snapshot: [v0.1.0-sprint1](https://github.com/Sprint-1-Software-engineering/Sprint-1/tree/v0.1.0-sprint1). This rewrite is a new review revision and does not replace that tag. Review it before creating a new release version.

## Submission and evaluator access

One member uploads one complete ZIP in Teams and adds the working repository URL to the submission description. Use the documents from the assessed release tag. Include the contribution file and check that all files and the diagram open.

In Settings → Collaborators / Collaborators and teams, keep `mhmttemin` and `goksuyldrm`, and add `nedima68`. Give all three at least Read access and verify accepted invitations. Public visibility does not replace this explicit named-account requirement. The ZIP does not need to be published as a public GitHub release attachment.
