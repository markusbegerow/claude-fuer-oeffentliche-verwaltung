# Skill-Veredelung: Anleitung zur Ueberarbeitung bestehender Skills

"Veredelung" bezeichnet die qualitative Ueberarbeitung eines bereits
bestehenden Skills (nicht das Neuanlegen). Ziel ist hoehere fachliche
Tiefe, bessere Quellenlage und praezisere Checklisten — ohne die
Grundstruktur aus `CLAUDE.md` Abschnitt 6 zu verletzen.

## Ablauf einer Veredelung

1. **Bestandsaufnahme.** Bestehende `SKILL.md` vollstaendig lesen.
   Pruefen: Sind alle sieben Pflichtabschnitte vorhanden? Ist die
   Quellenlage (Normen, Standards, Beschluesse) aktuell?
2. **Luecken identifizieren.** Fehlen Beispiele? Ist die Checkliste zu
   grob? Fehlt ein Stand-Datum?
3. **Ueberarbeiten, nicht ersetzen.** Bestehende korrekte Inhalte
   moeglichst erhalten, nur fehlerhafte oder veraltete Passagen ersetzen.
   Keine stillschweigende Aenderung der fachlichen Aussage ohne Begruendung
   im PR-Text.
4. **Quellenpruefung.** Jede neu eingefuegte Norm-, Standard- oder
   Beschlussangabe gegen `references/zitierweise-verwaltung.md` pruefen.
5. **Validieren.** `python scripts/validate_yaml_frontmatter.py` und
   `python scripts/validate_plugin_structure.py` ausfuehren.
6. **Index aktualisieren.** Falls sich Titel/Beschreibung aendern,
   `skills-index/<plugin>.md` und `SKILLS.md` entsprechend anpassen.

## Qualitaetskriterien fuer eine gelungene Veredelung

- Fachliche Tiefe steigt messbar (mehr Fallgruppen, praezisere
  Abgrenzungen).
- Keine neuen Blindzitate.
- Disclaimer- und Ausformulierungspflicht bleiben erhalten.
- Beispiel(e) sind durchgerechnet und nachvollziehbar.
