"""Structural validation of workshop assignments; not an answer checker."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = {
    "balicek-1-zaklad": 4,
    "balicek-2-stredni": 4,
    "balicek-3-pokrocily": 6,
    "balicek-humanitni": 6,
    "balicek-technicke": 6,
}
OUTPUTS = {
    "balicek-1-zaklad/projekt/kavarna-u-kopilota/dokumenty": {"README.md"},
    "balicek-2-stredni/projekt/pruzkum-spokojenosti/dokumenty": {"README.md"},
    "balicek-3-pokrocily/projekt/kvetinart-vytazky/vystupy": {"README.md"},
    "balicek-humanitni/projekt/seminar-kava-v-evrope/vystupy": {"README.md"},
    "balicek-technicke/projekt/znamkovy-kalkulator/docs": {"README.md", "maintainer-notes.md"},
}
REQUIRED_HEADINGS = ("## Vstupy a rozsah", "## Postup", "## Kritéria přijetí", "## Záznam a reflexe")
EXPECTED_AGENTS = {
    "balicek-2-stredni": {"redaktor"},
    "balicek-3-pokrocily": {"analytik", "redaktor"},
    "balicek-humanitni": {"prekladatel"},
    "balicek-technicke": {"revizor", "tester"},
}
EXPECTED_SKILLS = {
    "balicek-3-pokrocily": {"validace-dat", "tvorba-reportu"},
    "balicek-humanitni": {"shrnuti-zdroje"},
    "balicek-technicke": {"oprava-chyby"},
}


def forbidden_path(path: str) -> bool:
    parts = Path(path).parts
    return ".agent" in parts or Path(path).name.casefold() in {
        "reseni.md", "řešení.md", "quality_state.md", "decisions.md"
    }


def header(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError("missing YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    return data


def validate(root: Path = ROOT, distribution: bool = False, history: bool = False) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    files = [p for p in root.rglob("*") if p.is_file()
             and not any(part in {".git", ".venv", "__pycache__", ".pytest_cache"}
                         for part in p.relative_to(root).parts)]
    for path in files:
        if forbidden_path(path.relative_to(root).as_posix()):
            errors.append(f"Instructor-only file: {path.relative_to(root)}")
    try:
        manifest = json.loads((root / "workshop.json").read_text(encoding="utf-8"))
        tasks = manifest["tasks"]
        if manifest.get("schema_version") != 1 or not isinstance(tasks, list):
            raise ValueError("unsupported manifest")
        paths = [entry["path"] for entry in tasks]
        if len(paths) != len(set(paths)):
            errors.append("Duplicate task paths")
        for package, expected in PACKAGES.items():
            entries = [entry for entry in tasks if entry["package"] == package]
            if len(entries) != expected:
                errors.append(f"Task count differs for {package}")
            for entry in entries:
                expected_path = f"{package}/cviceni/{entry['task']}/uloha.md"
                if entry["path"] != expected_path:
                    errors.append(f"Task path mismatch: {entry['path']}")
        if len(tasks) != sum(PACKAGES.values()):
            errors.append("Total task count differs")
        actual_paths = {p.relative_to(root).as_posix() for p in root.glob("balicek-*/cviceni/*/uloha.md")}
        if actual_paths != set(paths):
            errors.append("Task manifest does not match assignment files")
        for relative in paths:
            path = (root / relative).resolve()
            if not path.is_relative_to(root) or not path.is_file():
                errors.append(f"Missing or invalid assignment: {relative}")
                continue
            text = path.read_text(encoding="utf-8")
            for heading in REQUIRED_HEADINGS:
                if heading not in text:
                    errors.append(f"Missing task section {heading}: {relative}")
    except (OSError, KeyError, TypeError, ValueError) as exc:
        errors.append(f"Invalid task manifest: {exc}")

    for package in PACKAGES:
        for relative in ("README.md", ".github/copilot-instructions.md", "teorie/README.md",
                         "reference/README.md", "kontrolni-sestavy/pred-balickem.md",
                         "kontrolni-sestavy/po-balicku.md"):
            if not (root / package / relative).is_file():
                errors.append(f"Missing package support: {package}/{relative}")

    for path in files:
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        body = re.sub(r"(?m)^```[^\n]*\n.*?^```[^\n]*(?:\n|$)", "", text, flags=re.S)
        for target in re.findall(r"\]\(([^)]+)\)", body):
            target = target.strip().strip("<>")
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            dest = (path.parent / target).resolve()
            if not dest.is_relative_to(root) or not dest.exists():
                errors.append(f"Invalid relative link: {path.relative_to(root)} -> {target}")
        if re.search(r"(?im)^#{1,6}\s+(?:Očekávané řešení|Expected solution)\b", body):
            errors.append(f"Answer-section marker: {path.relative_to(root)}")
        if path.name.endswith(".agent.md") or path.name == "SKILL.md" or path.name.endswith(".instructions.md"):
            try:
                data = header(path)
                if path.name.endswith(".instructions.md"):
                    if not isinstance(data.get("applyTo"), str) or not data["applyTo"].strip():
                        raise ValueError("applyTo must be a nonempty string")
                else:
                    for field in ("name", "description"):
                        if not isinstance(data.get(field), str) or not data[field].strip():
                            raise ValueError(f"{field} must be a nonempty string")
                if path.name.endswith(".agent.md"):
                    tools = data.get("tools")
                    if not isinstance(tools, list) or not all(isinstance(item, str) for item in tools):
                        raise ValueError("tools must be a YAML list of strings")
                    if data["name"] != path.name.removesuffix(".agent.md"):
                        raise ValueError("agent name must match filename")
                    for handoff in data.get("handoffs", []):
                        other = path.parent / f"{handoff['agent']}.agent.md"
                        if not other.is_file():
                            raise ValueError("handoff points to a missing agent")
                elif path.name == "SKILL.md" and data["name"] != path.parent.name:
                    raise ValueError("skill name must match directory")
            except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
                errors.append(f"Invalid configuration {path.relative_to(root)}: {exc}")

    try:
        inputs = json.loads((root / "vstupy.json").read_text(encoding="utf-8"))
        for entry in inputs["immutable_inputs"]:
            path = (root / entry["path"]).resolve()
            if not path.is_relative_to(root) or not path.is_file():
                errors.append(f"Missing input: {entry['path']}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
                errors.append(f"Changed input: {entry['path']}")
    except (OSError, KeyError, TypeError, ValueError) as exc:
        errors.append(f"Invalid input manifest: {exc}")

    if distribution:
        for directory, allowed in OUTPUTS.items():
            actual = {p.relative_to(root / directory).as_posix()
                      for p in (root / directory).rglob("*") if p.is_file()}
            if actual != allowed:
                errors.append(f"Distribution outputs differ: {directory}")
        for package in PACKAGES:
            agents = {p.name.removesuffix(".agent.md") for p in (root / package / ".github/agents").glob("*.agent.md")}
            skills = {p.parent.name for p in (root / package / ".github/skills").glob("*/SKILL.md")}
            if agents != EXPECTED_AGENTS.get(package, set()):
                errors.append(f"Unexpected supplied agents: {package}")
            if skills != EXPECTED_SKILLS.get(package, set()):
                errors.append(f"Unexpected supplied skills: {package}")
        starter_tests = root / "balicek-technicke/projekt/znamkovy-kalkulator/tests"
        if {p.name for p in starter_tests.glob("*.py")} != {"test_smoke.py"}:
            errors.append("Unexpected supplied behavioral tests")
        if list(root.glob("balicek-*/cviceni/*/prubeh.md")):
            errors.append("Participant records included in distribution")

    if history:
        result = subprocess.run(["git", "rev-list", "--all"], cwd=root, capture_output=True, text=True)
        if result.returncode:
            errors.append("Cannot inspect Git history")
        elif not result.stdout.strip():
            errors.append("No commits available for history inspection")
        else:
            for commit in result.stdout.splitlines():
                listing = subprocess.run(["git", "ls-tree", "-r", "--name-only", commit], cwd=root,
                                         capture_output=True, text=True)
                if listing.returncode:
                    errors.append(f"Cannot inspect commit {commit}")
                    continue
                for relative in listing.stdout.splitlines():
                    if forbidden_path(relative):
                        errors.append(f"Instructor-only file in commit {commit}: {relative}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--distribution", action="store_true", help="Check pristine workshop starter state")
    parser.add_argument("--history", action="store_true", help="Inspect all locally referenced commits")
    args = parser.parse_args()
    errors = validate(distribution=args.distribution, history=args.history)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: structure, links, YAML and immutable inputs" +
          ("; starter distribution" if args.distribution else "") +
          ("; locally referenced Git history" if args.history else ""))
    print("Manual review of teaching content and live VS Code configuration is still required.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
