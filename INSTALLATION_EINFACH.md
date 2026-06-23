# Installation fuer Einsteiger (Mac/Windows)

Diese Anleitung richtet sich an Personen ohne Entwicklungshintergrund, die
dieses Repository mit Claude Code nutzen wollen.

## Voraussetzungen

- Ein Anthropic-Konto mit Zugriff auf Claude Code.
- Git (zum Herunterladen des Repositories) oder alternativ: ZIP-Download
  ueber die "Code"-Schaltflaeche auf der Repository-Seite.

## Schritte unter Windows

1. Git installieren (falls nicht vorhanden): von der offiziellen
   Git-Webseite herunterladen und installieren.
2. Eingabeaufforderung oder PowerShell oeffnen.
3. In den gewuenschten Arbeitsordner wechseln.
4. Repository klonen oder ZIP entpacken.
5. Claude Code installieren/oeffnen und den entpackten Ordner als
   Arbeitsverzeichnis auswaehlen.
6. Pruefen, dass Claude Code die Plugins aus
   `.claude-plugin/marketplace.json` anzeigt.

## Schritte unter macOS

1. Terminal oeffnen.
2. Git ist auf macOS meist vorinstalliert; alternativ ueber Homebrew
   installieren.
3. In den gewuenschten Arbeitsordner wechseln und Repository klonen oder
   ZIP entpacken.
4. Claude Code oeffnen und den entpackten Ordner als Arbeitsverzeichnis
   auswaehlen.

## Erster Test

1. `QUICKSTART.md` befolgen.
2. Einen einfachen, fiktiven Beispielfall (z. B. "Pruefe den OZG-
   Umsetzungsstand einer fiktiven Verwaltungsleistung 'Wohngeldantrag'")
   mit dem Skill `ozg-umsetzung-pruefung` pruefen lassen.
3. Pruefen, ob die Ausgabe einen Disclaimer und ein Stand-Datum enthaelt.

## Haeufige Probleme

- **Plugin wird nicht erkannt:** Pruefen, ob der oberste ausgewaehlte
  Ordner tatsaechlich `.claude-plugin/marketplace.json` enthaelt.
- **Skill wird nicht gefunden:** Skill-Namen exakt wie in
  `skills-index/<plugin>.md` angeben.

Bei weiteren Problemen: Issue im Repository eroeffnen.
