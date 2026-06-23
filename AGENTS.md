# AGENTS.md — Kurzregeln fuer alle Werkzeuge

Dieses Dokument ist ein Auszug aus `CLAUDE.md` fuer Werkzeuge (z. B. Codex),
die nicht das volle Regelwerk einlesen. Es gilt zusaetzlich, nicht
ersatzweise zu `CLAUDE.md`.

## Pflichtregeln

1. **Sprache:** Deutsch, sofern nicht ausdruecklich anders gewuenscht.
2. **Gliederung:** Numerisch (1., 1.1, 1.2, ...) bei laengeren Pruefungen;
   keine reinen Stichpunkt-Endergebnisse.
3. **Quellen:** Keine Blindzitate. Siehe `references/zitierweise-verwaltung.md`.
4. **Disclaimer:** Jeder Output mit Rechts-, Datenschutz- oder
   IT-Sicherheitsbezug erhaelt den Hinweis aus `CLAUDE.md` Abschnitt 7
   (keine rechtliche/datenschutzrechtliche Einzelfallpruefung, keine
   verbindliche Behoerdenentscheidung).
5. **Skill-Frontmatter:** `name` (kebab-case, max. 64 Zeichen) und
   `description` (max. 1024 Zeichen, keine Kommas in Zahlen) — keine
   weiteren Frontmatter-Felder.
6. **Keine echten Buerger-, Mitarbeiter- oder Aktendaten und keine
   Zugangsdaten** in Beispielen oder Commits.
7. **Stand-Datum** in jedem inhaltlichen Output angeben.

## Vor jedem Commit

- `python scripts/validate_yaml_frontmatter.py`
- `python scripts/validate_plugin_structure.py`

Beide Skripte muessen fehlerfrei durchlaufen, bevor ein Commit oder PR
erstellt wird.
