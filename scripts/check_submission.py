"""Validate the design contract and its submission links. No runtime tests."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import yaml
from openapi_spec_validator import validate_spec
from openapi_schema_validator import OAS30Validator, oas30_format_checker

root = Path(__file__).resolve().parents[1]
required = ['README.md', 'LICENSE.md', 'CONTRIBUTIONS.md', 'docs/Project-Proposal-and-System-Vision.md', 'docs/Team-Members-and-RACI.md', 'docs/Git-Flow-Workflow.md', 'docs/Initial-Product-Backlog.md', 'docs/Openapi.yaml', 'docs/diagrams/system-boundary.svg']
for name in required:
    assert (root / name).is_file(), f"Missing {name}"

spec = yaml.safe_load((root / "docs/Openapi.yaml").read_text())
validate_spec(spec)

def resolved(value):
    if isinstance(value, dict):
        if "$ref" in value:
            target = spec
            for part in value["$ref"].removeprefix("#/").split("/"):
                target = target[part]
            return resolved(target)
        return {k: resolved(v) for k, v in value.items()}
    if isinstance(value, list):
        return [resolved(v) for v in value]
    return value

examples = 0
for name, schema in spec["components"]["schemas"].items():
    if "example" in schema:
        OAS30Validator(resolved(schema), format_checker=oas30_format_checker).validate(schema["example"])
        examples += 1

for response in spec["components"]["responses"].values():
    for media in response.get("content", {}).values():
        if "example" in media:
            OAS30Validator(resolved(media["schema"])).validate(media["example"])
            examples += 1

operations = [op for item in spec["paths"].values() for method, op in item.items() if method in {"get", "post", "patch", "delete"}]
ids = [op["operationId"] for op in operations]
assert len(ids) == len(set(ids)), "Duplicate operationId"
assert not any("/ai/" in path or "/parent/" in path for path in spec["paths"])
for path, method in [("/bookings", "post"), ("/bookings/{id}/status", "patch")]:
    codes = spec["paths"][path][method]["responses"]
    assert {"400", "401", "403", "404", "409"}.issubset(codes), path

backlog = (root / "docs/Initial-Product-Backlog.md").read_text()
for entry in re.findall(r"API: `([^`]+)`", backlog):
    for endpoint in entry.split(";"):
        method, path = endpoint.strip().split(" ", 1)
        assert method.lower() in spec["paths"].get(path, {}), f"Missing backlog API: {endpoint}"

for file in list(root.rglob("*.md")):
    if ".git" in file.parts:
        continue
    for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", file.read_text()):
        if "://" in link or link.startswith("#"):
            continue
        target = link.split("#")[0]
        assert (file.parent / target).exists(), f"Broken link in {file.name}: {link}"

ET.parse(root / "docs/diagrams/system-boundary.svg")
raci = (root / "docs/Team-Members-and-RACI.md").read_text().split("## RACI", 1)[1].split("## Peer review", 1)[0]
for line in raci.splitlines():
    cells = [x.strip() for x in line.split("|")[1:-1]]
    if len(cells) != 7 or cells[0] == "Work" or set(cells[0]) == {"-"}:
        continue
    assert sum("A" in x.split("/") for x in cells[1:]) == 1, line
    assert any("R" in x.split("/") for x in cells[1:]), line

print(f"PASS: OpenAPI 3.0.3, {len(operations)} operations, {examples} examples, document links, diagram XML and RACI.")
print("Not checked: interviews, deployed behavior, individual work, peer approvals, access, protections or final release.")
