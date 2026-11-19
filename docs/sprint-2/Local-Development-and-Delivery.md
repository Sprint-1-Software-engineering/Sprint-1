# Local Development and Delivery

Owner: Osman Berke Özdemir (@makucheez). Tracking: [#63](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/63).
Status: verified local reference procedure; backend adoption and integration await team review.

## Baselines and technology decision

- `develop` at `1e50523cda7b06ece5b5be4927353390c4aab562` has static frontend files and document validation, but no `src/server.py`.
- [PR #58](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/58), pinned at `7f3fa7735987dc59bc54be5257f9e2145c529a1c`, contains the local Python/SQLite auth prototype. It is not merged into develop. Its target was main at the 19 November review; the author needs to reconcile this with the documented feature -> develop workflow.
- Recommendation for architecture review: keep Python/SQLite for the small local prototype to reuse the working auth code. This is Osman's proposal, not an approved team technology change. Mehmet and Toprak own resolution of OD-01/OD-02 in the [requirements PR #62](https://github.com/Sprint-1-Software-engineering/Sprint-1/pull/62).
- Current executable behavior is Python standard-library HTTP + SQLite, opaque database-backed bearer sessions, `http://127.0.0.1:8000/api/v1`. Node/Express, JWT and port 3000 remain conflicting historical design descriptions, not a second running backend. Update SRS/OpenAPI/architecture together after approval; do not silently overwrite those owners' work.

## Requirements and dependencies

Git, a browser and Python 3 are needed. The reference was actually verified with Python 3.9.6 / SQLite supplied by Python on macOS; The pinned reference smoke also passed in CI with Python 3.12.16 on Ubuntu; CI tooling targets Python 3.12. See [actual results](Verification-Report.md) for the CI evidence and its scope. No supported-version matrix beyond tested environments is claimed. Python must include `sqlite3`; check with:

```sh
python3 --version
python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
```

The application imports only the Python standard library: no npm install, external database server, API key or third-party runtime package is required. `.env` is not loaded; `.env.example` intentionally contains comments only. Host, port and database path are hard-coded in this reference; setting PORT or DATABASE_URL has no effect.

## Obtain a clean reference and run it

Use a fresh destination; do not replace an existing checkout or reset another member's work. These commands intentionally reproduce the unmerged PR snapshot, rather than claiming develop already includes the server.

```sh
git clone https://github.com/Sprint-1-Software-engineering/Sprint-1.git TutorBridge-auth-reference
cd TutorBridge-auth-reference
git switch --detach 7f3fa7735987dc59bc54be5257f9e2145c529a1c
python3 src/server.py
```

Windows: use `py -3` instead of `python3` if that is your installed launcher. It has not been independently tested on Windows. Once #58 is reviewed and integrated, use the reviewed develop/release commit instead of the pinned reference and rerun verification.

Open [registration](http://127.0.0.1:8000/register.html), then [login](http://127.0.0.1:8000/login.html). Use synthetic data, a teacher/student role and a 12-128-character password. Current screen text is inconsistent about password length; the server enforces 12-128 at registration. The dashboard contains sample data. These steps are for local demonstration, not a production deployment.

## Startup, storage, shutdown and reset

The server creates `data/tutorbridge.db` relative to the checkout, including its parent directory, on the first start. It initializes `users`, `auth_tokens` and an index. Accounts persist on disk. Tokens are stored with expiry; they are valid for one hour and remain on disk across restart until expired/cleaned. A successful login invalidates earlier tokens for that user. Database files are outside the served `src` directory.

The listener binds only `127.0.0.1:8000`. Keep the server terminal open; use Ctrl+C to stop it. If port 8000 is occupied, stop the known existing process or use a different isolated machine. There is no supported port configuration in this snapshot. Do not kill unknown processes.

Restart with the same command to retain accounts. To reset a disposable demo, stop the server and move `data/tutorbridge.db` to a private backup outside the repository; startup creates a new database. Do not reset real user data. See [backup/restore design](Deployment-and-Recovery.md). Never commit databases, tokens, uploads or backups.

## Implemented HTTP operations and limitations

| Operation (prefix `/api/v1`) | Current reference behavior |
|---|---|
| POST /auth/register | Creates teacher/student accounts; salted PBKDF2 password hash; duplicate email 409 |
| POST /auth/login | Valid credentials return opaque bearer token and expiresIn 3600; wrong password 401 |
| GET /users/me | Returns own public profile; missing/invalid/expired bearer token 401 |

Other designed invitation/availability/booking/assignment operations are not implemented here. Do not infer implementation from OpenAPI. The sample dashboard, teacher routing, placeholder links and browser-only logout are not accepted full product flows. Invalid email and null-name validation defects remain open in #58's source; the current contract says JWT although the code uses opaque tokens. The frontend assumes the fixed local address and has CORS limitations outside the documented same-origin URL. No browser E2E, production security or deployed-system success is claimed.

## Repeatable checks from the DevOps branch

Keep the auth reference in a separate directory. From the checkout containing this DevOps change:

```sh
python3 -m venv /tmp/tutorbridge-docs-venv
/tmp/tutorbridge-docs-venv/bin/python -m pip install -r requirements-docs.txt
/tmp/tutorbridge-docs-venv/bin/python scripts/check_submission.py
python3 scripts/check_sprint2.py
python3 -m unittest discover -s tests -v
python3 scripts/check_auth_environment.py --source-root ../TutorBridge-auth-reference --report /tmp/auth-environment.json
python3 scripts/check_auth_environment.py --source-root ../TutorBridge-auth-reference --validation-probes --report /tmp/auth-validation.json
```

Use a user-selected temporary directory and its Python executable on Windows. The last command is expected to exit 1 while the two input defects remain; this is an actual failed acceptance probe, not a passing test. The checker copies only `src` into new temporary storage, starts the real server, uses synthetic accounts, stops it and removes generated data. It does not touch the reference checkout's database. Port 8000 must be free. Without `--source-root`, the script requires a server in the current checkout and exits with an error when absent.

The unchanged `Sprint 1 checks` remains the existing required context. Sprint 2 structural checks do not imply complete team deliverables; `python3 scripts/check_sprint2.py --release-ready` also fails on missing proposed team document paths. The check does not inspect external-link access or prose quality. CI's integrated auth job is skipped explicitly when `src/server.py` is absent. A separately named pinned PR #58 job checks only the reference snapshot. No Berat/Mehmet automated test suite existed in the reviewed trees; integrate their agreed test command when one is actually authored, including its dependencies. This environment smoke is Osman's infrastructure verification and does not replace QA acceptance or coverage.

## Independent reproduction and delivery

Mehmet should repeat the clean-start procedure and Berat should inspect the failed probes and smoke/acceptance boundary. No independent teammate run has yet been recorded. Record actual name, date, commit, environment and observations after it happens. Review [submission gates](Submission-Checklist.md) before release. Never publish a reference snapshot as the final Sprint 2 submission.
