# TutorBridge

SENG 321 · Sprint 1

A web application for private tutors and their existing students. The first release covers student invitations, lesson scheduling and assignment sharing.

## Sprint 1 documents

- [Project Proposal and System Vision](docs/Project-Proposal-and-System-Vision.md)
- [System Boundary Diagram](docs/diagrams/system-boundary.svg)
- [Team Members and RACI](docs/Team-Members-and-RACI.md)
- [OpenAPI Draft](docs/Openapi.yaml)
- [Initial Product Backlog](docs/Initial-Product-Backlog.md)
- [Git-Flow Workflow](docs/Git-Flow-Workflow.md)
- [Individual Contributions](CONTRIBUTIONS.md)
- [Submission Status](docs/Submission.md)

## Planned stack

HTML, CSS and JavaScript; Node.js with Express; SQLite. This is a planning submission. The files in `src/` are placeholders, not a working application.

AI features, parent accounts, payments, video and teacher discovery are outside the MVP.

## Validate the documents

Use Python 3.12 or newer in a virtual environment:

```sh
python -m pip install -r requirements-docs.txt
python scripts/check_submission.py
```

The same check runs on PRs and pushes. Passing it validates the contract and document structure, not user research or runtime behavior.

## Submission

The six foundation documents are prepared for team review. Branch protection is active. Interviews, each member's real contribution evidence, named evaluator access and the reviewed main release still need completion before submission. See [Submission Status](docs/Submission.md).

License: [MIT](LICENSE.md).
