"""Latency baseline for the local TutorBridge auth API (QA, not an acceptance test).

Usage: python scripts/measure_auth_latency.py [report.json]
Starts the src/server.py handler on a random localhost port with a temporary
SQLite database and times requests from the same machine. Only synthetic
accounts are used. Results depend on the machine and are a baseline for
docs/sprint-2/NFR-and-Quality-Measures.md (PERF-01, PERF-02), not an acceptance test.
"""
import importlib.util
import json
import os
import platform
import statistics
import sys
import tempfile
import threading
import time
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else None

spec = importlib.util.spec_from_file_location("tb_server", REPO / "src" / "server.py")
srv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(srv)
tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
srv.DATABASE_PATH = Path(tmp.name) / "data" / "tutorbridge.db"
srv.initialize_database()
os.chdir(REPO / "src")


class Handler(srv.TutorBridgeHandler):
    def log_message(self, *a):
        pass


class Server(ThreadingHTTPServer):
    daemon_threads = True


httpd = Server(("127.0.0.1", 0), Handler)
PORT = httpd.server_address[1]
threading.Thread(target=httpd.serve_forever, daemon=True).start()
PW = "Example-only-123"


def call(method, path, payload=None, token=None):
    c = HTTPConnection("127.0.0.1", PORT, timeout=30)
    h = {}
    body = None
    if payload is not None:
        body = json.dumps(payload)
        h["Content-Type"] = "application/json"
    if token:
        h["Authorization"] = "Bearer " + token
    t0 = time.perf_counter()
    c.request(method, path, body=body, headers=h)
    r = c.getresponse()
    data = r.read()
    ms = (time.perf_counter() - t0) * 1000
    c.close()
    return r.status, ms, data


def pct(values, p):
    s = sorted(values)
    k = max(0, min(len(s) - 1, int(round(p / 100 * len(s) + 0.5)) - 1))
    return s[k]


def summarize(name, ms, errors, concurrency):
    return {"operation": name, "requests": len(ms) + errors, "concurrency": concurrency, "errors": errors,
            "p50_ms": round(statistics.median(ms), 1), "p95_ms": round(pct(ms, 95), 1), "max_ms": round(max(ms), 1)}


def run(name, n, concurrency, fn, expected_status):
    times, errs = [], [0]
    lock = threading.Lock()
    per_thread = n // concurrency

    def worker(idx):
        for i in range(per_thread):
            st, ms, _ = fn(idx, i)
            with lock:
                if st == expected_status:
                    times.append(ms)
                else:
                    errs[0] += 1

    ths = [threading.Thread(target=worker, args=(i,)) for i in range(concurrency)]
    [t.start() for t in ths]
    [t.join() for t in ths]
    return summarize(name, times, errs[0], concurrency)


results = []
# registration (sequential, unique e-mails)
results.append(run("POST /auth/register", 30, 1,
                   lambda w, i: call("POST", "/api/v1/auth/register",
                                     {"name": "Perf User", "email": f"perf{i}@example.test", "password": PW, "role": "student"})[:3],
                   201))
# login
results.append(run("POST /auth/login", 30, 1,
                   lambda w, i: call("POST", "/api/v1/auth/login", {"email": f"perf{i}@example.test", "password": PW}), 200))
results.append(run("POST /auth/login", 30, 5,
                   lambda w, i: call("POST", "/api/v1/auth/login", {"email": f"perf{w * 6 + i}@example.test", "password": PW}), 200))
# profile with one token per concurrent worker
tokens = []
for w in range(10):
    st, _, data = call("POST", "/api/v1/auth/login", {"email": f"perf{w}@example.test", "password": PW})
    tokens.append(json.loads(data)["accessToken"])
results.append(run("GET /users/me", 200, 1, lambda w, i: call("GET", "/api/v1/users/me", token=tokens[0]), 200))
results.append(run("GET /users/me", 500, 10, lambda w, i: call("GET", "/api/v1/users/me", token=tokens[w]), 200))
httpd.shutdown()

info = {"python": platform.python_version(), "os": platform.platform(), "processor": platform.processor(),
        "cpu_count": os.cpu_count(), "note": "single run, one developer machine, loopback, temporary SQLite DB"}
if OUT is not None:
    OUT.write_text(json.dumps({"environment": info, "results": results}, indent=1), encoding="utf-8")
print(json.dumps(info))
for r in results:
    print(f"{r['operation']:<22} n={r['requests']:<4} conc={r['concurrency']:<3} err={r['errors']} "
          f"p50={r['p50_ms']} ms  p95={r['p95_ms']} ms  max={r['max_ms']} ms")
