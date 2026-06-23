#!/usr/bin/env python3
"""Validate that every plugin referenced in marketplace.json has a
valid plugin.json and a non-empty skills/ directory."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_PLUGIN_FIELDS = ["name", "version", "description", "license", "author"]


def main() -> int:
    errors = []
    manifest_path = ROOT / ".claude-plugin" / "marketplace.json"

    if not manifest_path.exists():
        print(f"Manifest nicht gefunden: {manifest_path}")
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    plugins = manifest.get("plugins", [])
    if not plugins:
        errors.append("marketplace.json enthaelt keine Plugins")

    for plugin_entry in plugins:
        source = plugin_entry.get("source", "")
        plugin_dir = (ROOT / source).resolve() if source else None

        if plugin_dir is None or not plugin_dir.is_dir():
            errors.append(f"Plugin-Ordner fehlt fuer source={source!r}")
            continue

        plugin_json_path = plugin_dir / ".claude-plugin" / "plugin.json"
        if not plugin_json_path.exists():
            errors.append(f"{plugin_dir}: .claude-plugin/plugin.json fehlt")
        else:
            plugin_data = json.loads(plugin_json_path.read_text(encoding="utf-8"))
            for field in REQUIRED_PLUGIN_FIELDS:
                if field not in plugin_data:
                    errors.append(f"{plugin_json_path}: Feld '{field}' fehlt")

        skills_dir = plugin_dir / "skills"
        if not skills_dir.is_dir() or not any(skills_dir.iterdir()):
            errors.append(f"{plugin_dir}: 'skills/' fehlt oder ist leer")
        else:
            for skill_dir in skills_dir.iterdir():
                if skill_dir.is_dir() and not (skill_dir / "SKILL.md").exists():
                    errors.append(f"{skill_dir}: SKILL.md fehlt")

    if errors:
        print(f"{len(errors)} Fehler gefunden:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"OK: {len(plugins)} Plugins valide strukturiert.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
