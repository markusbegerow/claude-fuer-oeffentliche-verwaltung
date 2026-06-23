# CLAUDE.md — Verbindliches Regelwerk

Dieses Dokument gilt fuer jedes Modell und jeden Agenten (Claude, Codex,
sonstige LLM-Werkzeuge), das in diesem Repository Skills nutzt, erweitert
oder pflegt. Es ist ein eigenstaendiges Regelwerk fuer das Themenfeld
**Digitalisierung, Fachverfahren und Organisation der oeffentlichen
Verwaltung (Deutschland)** und kein Abdruck eines fremden Regelwerks.

## 1. Geltungsbereich und Zweck

Dieses Repository stellt Claude-Code-Skills bereit, die Angestellte und
Beamtinnen/Beamte in deutschen Behoerden beim **strukturierten Pruefen**
verwaltungsbezogener Digitalisierungs-, Fachverfahrens- und
Organisationsfragen unterstuetzen. Es ist ein technisches Experimentierfeld
fuer Verwaltungsmitarbeitende, IT-Verantwortliche, Organisationsentwicklung
und informierte Buergerinnen/Buerger — **kein Ersatz** fuer eine individuelle
Rechtsberatung, eine datenschutzrechtliche Pruefung, eine
IT-sicherheitsrechtliche Bewertung oder eine verbindliche Entscheidung der
zustaendigen Behoerde.

## 2. Sprache

- Alle Skill-Inhalte, READMEs und Outputs sind auf **Deutsch** verfasst,
  sofern der Nutzer nicht ausdruecklich Englisch verlangt.
- Fachbegriffe (z. B. "Once-Only", "Smart Government", "E-Government") werden
  in der gebraeuchlichen Form verwendet, aber im Kontext deutsch erlaeutert.

## 3. Methodik

- Jede Pruefung folgt der Methodik aus
  `references/methodik-verwaltungspruefung.md` (Sachverhaltsaufbereitung,
  Einordnung, Pruefschema, foederale/technische Pruefung, Ausformulierung).
- Zwischenergebnisse werden klar als solche markiert.
- Unsicherheiten in der Sachverhaltsaufnahme werden durch konkrete
  Rueckfragen an den Nutzer aufgeloest, statt Annahmen unausgesprochen zu
  treffen.

## 4. Quellen- und Zitierpflicht

- Verbindlich ist `references/zitierweise-verwaltung.md`. Kein Blindzitat aus
  reinem Modellwissen — siehe dort die harten Sperren.
- Jeder Skill-Output nennt ein **Stand-Datum**.
- Themen-Anker zur Recherche-Orientierung liefert
  `references/leitentscheidungen-verwaltung.md` — das sind keine fertig
  geprueften Zitate, sondern Sucheinstiege.

## 5. Gliederung und Ausformulierung

- Skill-Outputs werden in vollstaendigen Saetzen ausformuliert, nicht als
  reine Stichpunktliste.
- Numerische Gliederung (1., 1.1, 1.2, ...) fuer laengere Pruefberichte;
  kurze Antworten duerfen ohne Gliederung bleiben, wenn der Sachverhalt es
  zulaesst.
- Tabellen sind erlaubt, wo sie Lesbarkeit erhoehen (z. B. Zustaendigkeits-
  Uebersicht, Standard-Vergleich), ersetzen aber nicht die Ausformulierung
  des Ergebnisses.

## 6. Skill-Konvention (`SKILL.md`)

Jeder Skill liegt unter `skills/<skill-name>/SKILL.md` innerhalb eines
Plugin-Ordners und hat folgendes YAML-Frontmatter:

```yaml
---
name: <kebab-case-name, max. 64 Zeichen>
description: "<Zweck in max. 1024 Zeichen, keine Kommas in Zahlen>"
---
```

Der Markdown-Koerper enthaelt mindestens folgende Abschnitte in dieser
Reihenfolge:

1. **Zweck / Anwendungsfall** — wann wird dieser Skill genutzt?
2. **Eingaben** — welche Angaben/Unterlagen muss der Nutzer mitbringen?
3. **Ablauf / Checkliste** — Schritt-fuer-Schritt-Pruefung.
4. **Quellenpflicht** — Verweis auf `../../../references/zitierweise-verwaltung.md`.
5. **Ausgabeformat** — Ausformulierungspflicht, Stand-Datum,
   verbotene Formate (reine Stichpunkt-Skelette als Endergebnis).
6. **Beispiele** — mindestens ein durchgerechnetes Beispiel.
7. **Normen und Standards** — kuratierte Liste der einschlaegigen
   Gesetze, Verordnungen, Standards oder Beschluesse fuer dieses Thema.

## 7. Disclaimer-Pflicht

Jede `README.md` (Root und Plugin-Ebene) und jede `SKILL.md` beginnt mit
einem klar erkennbaren Hinweis:

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

Zusaetzlich wird bei sicherheits- bzw. blaulichtbezogenen Themen darauf
hingewiesen, dass keine operative Einsatztaktik vermittelt wird, sondern
ausschliesslich organisatorische und kommunikative Ablaufhilfen, und bei
foederalen/technischen Themen auf die laufende Weiterentwicklung von
Standards (OZG-Umsetzung, IT-Planungsrat-Beschluesse, BSI-Grundschutz)
hingewiesen.

## 8. Datenschutz und Fall-/Personendaten

- Keine echten Buerger-, Mitarbeiter- oder Aktendaten in Beispielen,
  Testfaellen oder Commits. Ausschliesslich fiktive, klar als solche
  gekennzeichnete Beispieldaten.
- Keine Zugangsdaten, Passwoerter oder sonstigen sicherheitsrelevanten
  Geheimnisse in jedweder Form in diesem Repository — auch nicht als
  Beispiel.

## 9. Versionierung

- Versionsschema `MAJOR.MINOR.PATCH`, beginnend bei `001.0.0` fuer dieses
  Projekt.
- Aenderungen werden in `CHANGELOG.md` dokumentiert.

## 10. Git-Workflow

- Aussagekraeftige Commit-Nachrichten auf Deutsch.
- Kein Force-Push auf den Hauptzweig.
- Vor jedem Merge: `python scripts/validate_yaml_frontmatter.py` und
  `python scripts/validate_plugin_structure.py` fehlerfrei durchlaufen
  lassen.
