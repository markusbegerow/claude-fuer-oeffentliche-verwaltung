#!/usr/bin/env python3
"""Validate that every SKILL.md has well-formed YAML frontmatter.

Checks performed for each skills/<name>/SKILL.md:
- starts with '---' frontmatter block containing 'name' and 'description'
- name is kebab-case, <= 64 ASCII characters, matches the folder name
- description is a non-empty string, <= 1024 characters
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install -r requirements.txt")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
KEBAB_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def extract_frontmatter(text: str):
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1]


def main() -> int:
    errors = []
    skill_files = sorted(ROOT.glob("*/skills/*/SKILL.md"))
    if not skill_files:
        print("Keine SKILL.md-Dateien gefunden.")
        return 1

    for skill_file in skill_files:
        folder_name = skill_file.parent.name
        text = skill_file.read_text(encoding="utf-8")
        raw_frontmatter = extract_frontmatter(text)
        if raw_frontmatter is None:
            errors.append(f"{skill_file}: kein YAML-Frontmatter gefunden")
            continue
        try:
            data = yaml.safe_load(raw_frontmatter) or {}
        except yaml.YAMLError as exc:
            errors.append(f"{skill_file}: ungueltiges YAML ({exc})")
            continue

        name = data.get("name")
        description = data.get("description")

        if not name:
            errors.append(f"{skill_file}: Feld 'name' fehlt")
        elif name != folder_name:
            errors.append(
                f"{skill_file}: 'name' ({name}) entspricht nicht dem Ordnernamen ({folder_name})"
            )
        elif not KEBAB_RE.match(name) or len(name) > 64:
            errors.append(f"{skill_file}: 'name' ist kein gueltiges kebab-case (<=64 Zeichen)")

        if not description:
            errors.append(f"{skill_file}: Feld 'description' fehlt")
        elif len(description) > 1024:
            errors.append(f"{skill_file}: 'description' laenger als 1024 Zeichen")

    if errors:
        print(f"{len(errors)} Fehler gefunden:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"OK: {len(skill_files)} SKILL.md-Dateien valide.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
