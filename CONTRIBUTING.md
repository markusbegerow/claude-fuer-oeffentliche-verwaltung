# Beitragen

Danke fuer dein Interesse an diesem Repository. Bitte beachte vor einem
Pull Request folgende Checkliste.

## PR-Checkliste

- [ ] Inhalte auf Deutsch (siehe `CLAUDE.md` Abschnitt 2).
- [ ] Zitierweise nach `references/zitierweise-verwaltung.md` eingehalten.
- [ ] Methodik nach `references/methodik-verwaltungspruefung.md` eingehalten.
- [ ] `SKILL.md`-Frontmatter vollstaendig (`name`, `description`) und
      regelkonform (siehe `CLAUDE.md` Abschnitt 6).
- [ ] Disclaimer-Hinweis vorhanden (siehe `CLAUDE.md` Abschnitt 7).
- [ ] Keine echten Buerger-, Mitarbeiter- oder Aktendaten, keine
      Zugangsdaten.
- [ ] `python scripts/validate_yaml_frontmatter.py` laeuft fehlerfrei.
- [ ] `python scripts/validate_plugin_structure.py` laeuft fehlerfrei.
- [ ] Bei neuen Skills: Eintrag in der passenden `skills-index/*.md` und in
      `SKILLS.md` ergaenzt.

## Neuen Skill anlegen

1. Ordner `<plugin>/skills/<skill-name>/` anlegen.
2. `SKILL.md` nach dem Muster in `CLAUDE.md` Abschnitt 6 schreiben.
3. Validierungsskripte laufen lassen.
4. Eintrag in `skills-index/<plugin>.md` und `SKILLS.md` ergaenzen.

## Neues Plugin anlegen

1. Ordner `<plugin-name>/` mit `.claude-plugin/plugin.json`, `README.md`,
   `skills/` anlegen.
2. Eintrag in `.claude-plugin/marketplace.json` ergaenzen.
3. `skills-index/<plugin-name>.md` anlegen.

## Code of Conduct

Es gilt der `CODE_OF_CONDUCT.md`.
