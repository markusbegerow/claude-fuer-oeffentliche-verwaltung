#!/usr/bin/env python3
"""Regenerate SKILLS.md from the name/description frontmatter of every
SKILL.md, grouped by plugin. Run after adding or renaming a skill."""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install -r requirements.txt")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent


def extract_frontmatter(text: str):
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def main() -> int:
    plugin_dirs = sorted(
        p.parent for p in ROOT.glob("*/skills") if p.is_dir()
    )

    lines = ["# SKILLS.md — Flacher Index aller Skills", ""]
    lines.append("Format: `<plugin>:<skill-name>` — Beschreibung")
    lines.append("")

    for plugin_dir in plugin_dirs:
        plugin_name = plugin_dir.name
        lines.append(f"## {plugin_name}")
        lines.append("")
        skill_files = sorted((plugin_dir / "skills").glob("*/SKILL.md"))
        for skill_file in skill_files:
            data = extract_frontmatter(skill_file.read_text(encoding="utf-8"))
            name = data.get("name", skill_file.parent.name)
            description = (data.get("description") or "").strip()
            title = description.split(".")[0] if description else ""
            lines.append(f"- `{plugin_name}:{name}` — {title}")
        lines.append("")

    output_path = ROOT / "SKILLS.md"
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"SKILLS.md aktualisiert ({output_path}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
