"""Exercise the real local server in disposable storage; never log credentials.

Basic smoke checks are deliberately narrower than story acceptance. Add
--validation-probes to enforce two known input acceptance criteria as well.
"""
import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import platform
import shutil
import socket
import sqlite3
import subprocess
import sys
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--report", type=Path)
    parser.add_argument("--validation-probes", action="store_true")
    args = parser.parse_args()
    source = args.source_root.resolve()
    if not (source / "src/server.py").is_file():
        parser.error("src/server.py is absent; runtime verification is unavailable, not passed")
    # The reviewed server binds this fixed port. Do not contact an existing app.
    with socket.socket() as guard:
        guard.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            guard.bind(("127.0.0.1", 8000))
        except OSError:
            parser.error("port 8000 is busy; stop the existing server before testing")
    cases = []
    report = {
        "python": platform.python_version(), "platform": platform.platform(),
        "source_root": str(source), "validation_probes": args.validation_probes,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(), "cases": cases,
        "scope": "Local server startup, basic auth, storage and restart; no browser/E2E or full story acceptance",
    }

    def check(name, ok):
        cases.append({"name": name, "passed": bool(ok)})
        print(("PASS: " if ok else "FAIL: ") + name)

    with tempfile.TemporaryDirectory(prefix="tutorbridge-auth-") as directory:
        root = Path(directory)
        shutil.copytree(source / "src", root / "src", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        db = root / "data/tutorbridge.db"
        process = None

        def request(path, data=None, token=None):
            headers = {"Content-Type": "application/json"}
            if token is not None:
                headers["Authorization"] = "Bearer " + token
            req = Request("http://127.0.0.1:8000" + path,
                          data=None if data is None else json.dumps(data).encode(), headers=headers)
            try:
                response = urlopen(req, timeout=5)
            except HTTPError as error:
                response = error
            with response:
                body = response.read()
                content = response.headers.get("Content-Type", "")
                return response.code, json.loads(body) if "application/json" in content else None

        def start(log):
            child = subprocess.Popen([sys.executable, "src/server.py"], cwd=root,
                                     stdout=log, stderr=log)
            try:
                deadline = time.monotonic() + 10
                while time.monotonic() < deadline:
                    if child.poll() is not None:
                        raise RuntimeError("server exited during startup")
                    try:
                        if request("/login.html")[0] == 200:
                            return child
                    except (URLError, TimeoutError, ConnectionError):
                        pass
                    time.sleep(0.1)
                raise RuntimeError("server startup timed out")
            except BaseException:
                stop(child)
                raise

        def stop(child):
            if child is not None and child.poll() is None:
                child.terminate()
                try:
                    child.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    child.kill()
                    child.wait(timeout=5)

        with (root / "server.log").open("wb") as log:
            try:
                process = start(log)
                check("registration page served", request("/register.html")[0] == 200)
                check("login page served", request("/login.html")[0] == 200)
                with sqlite3.connect(db) as connection:
                    tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
                check("first startup creates users and auth_tokens", {"users", "auth_tokens"} <= tables)
                account = {"name": "Environment Check", "email": "environment@example.test",
                           "password": "Synthetic-check-123!", "role": "student"}
                status, user = request("/api/v1/auth/register", account)
                check("valid registration returns public profile", status == 201 and set(user) == {"id", "name", "email", "role"})
                check("duplicate email rejected", request("/api/v1/auth/register", account)[0] == 409)
                check("short password rejected", request("/api/v1/auth/register", dict(account, email="short@example.test", password="short"))[0] == 400)
                check("invalid role rejected", request("/api/v1/auth/register", dict(account, email="role@example.test", role="parent"))[0] == 400)
                credentials = {"email": account["email"], "password": account["password"]}
                check("wrong password rejected", request("/api/v1/auth/login", dict(credentials, password="incorrect"))[0] == 401)
                status, session = request("/api/v1/auth/login", credentials)
                token = session.get("accessToken", "")
                check("login returns one-hour bearer token", status == 200 and bool(token) and session.get("expiresIn") == 3600 and session.get("tokenType") == "Bearer")
                status, profile = request("/api/v1/users/me", token=token)
                check("valid token reads own public profile", status == 200 and profile == user)
                check("missing token rejected", request("/api/v1/users/me")[0] == 401)
                check("invalid token rejected", request("/api/v1/users/me", token="synthetic-invalid-token")[0] == 401)
                with sqlite3.connect(db) as connection:
                    connection.execute("UPDATE auth_tokens SET expires_at = ? WHERE token = ?",
                                       ((datetime.now(timezone.utc) - timedelta(seconds=1)).isoformat(), token))
                check("expired token rejected", request("/api/v1/users/me", token=token)[0] == 401)
                check("database is outside served static directory", request("/data/tutorbridge.db")[0] == 404)
                if args.validation_probes:
                    check("invalid email rejected (acceptance probe)", request("/api/v1/auth/register", dict(account, email="bad@@example.com"))[0] == 400)
                    check("null name rejected (acceptance probe)", request("/api/v1/auth/register", dict(account, email="null@example.test", name=None))[0] == 400)
                stop(process)
                process = start(log)
                check("account survives stop and restart", request("/api/v1/auth/login", credentials)[0] == 200)
            finally:
                stop(process)
    report["passed"] = sum(case["passed"] for case in cases)
    report["failed"] = len(cases) - report["passed"]
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Result: {report['passed']} passed, {report['failed']} failed; disposable data removed.")
    return bool(report["failed"])


if __name__ == "__main__":
    sys.exit(main())
