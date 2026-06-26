# Claude Skills für die Öffentliche Verwaltung

<p align="center">
<img alt="claude-fuer-oeffentliche-verwaltung" src="https://github.com/user-attachments/assets/3630444d-df83-4d9c-bcb2-cd2d693df479" />
</p>

> **Wichtiger Hinweis:** Dieses Repository ist eine experimentelle
> Sammlung von Claude-Code-Skills zu Digitalisierung, Fachverfahren und
> Organisation der oeffentlichen Verwaltung in Deutschland. Es ersetzt
> **keine** rechtliche, datenschutzrechtliche oder IT-sicherheitsrechtliche
> Einzelfallpruefung durch die zustaendige Fachstelle und **keine**
> verbindliche Entscheidung der zustaendigen Behoerde. Alle Ausgaben sind
> Arbeitshilfen ohne Gewaehr. Jede Nutzerin und jeder Nutzer traegt die
> alleinige Verantwortung fuer die Verwendung der erzeugten Inhalte und
> sollte im Einzelfall die zustaendige Fachaufsicht, die bzw. den
> Datenschutzbeauftragten oder die Rechtsabteilung konsultieren.

## Worum geht es?

Dieses Repository stellt drei Claude-Code-Plugins mit Skills bereit, die
Angestellte und Beamtinnen/Beamte in deutschen Behoerden beim strukturierten
Pruefen verwaltungsbezogener Digitalisierungs-, Fachverfahrens- und
Organisationsfragen unterstuetzen:

| Plugin | Fokus |
|---|---|
| [`verwaltung-digitalisierung-ki`](verwaltung-digitalisierung-ki/README.md) | Digitale Verwaltung und Staatsmodernisierung (OZG, FIT-Connect, FIM, digitale Identitaeten, elektronische Signaturen, KI-Einsatz, Registermodernisierung, Interoperabilitaet, Barrierefreiheit, Deutschland-Stack) |
| [`verwaltung-fachverfahren-kommune`](verwaltung-fachverfahren-kommune/README.md) | Fachverfahren der Kommunalverwaltung und Buergerdienste (Einwohnermeldeamt, Standesamt, Auslaenderbehoerde, Wahlamt, kommunales Finanzwesen, Buergerportale) |
| [`verwaltung-organisation-sicherheit`](verwaltung-organisation-sicherheit/README.md) | Organisationsentwicklung, foederale Zusammenarbeit, Wissensmanagement und Sicherheit/Blaulicht (Changemanagement, Weiterbildung, Laenderkooperation, Krisenmanagement) |

Dieses Projekt ist als MVP angelegt und wird iterativ um weitere Plugins
und Skills erweitert (siehe `CHANGELOG.md`). Die Themengrundlage findet
sich in `oeffentliche-verwaltung-themen.md`.

## Schnelleinstieg

1. `QUICKSTART.md` lesen (2 Minuten).
2. Repository in Claude Code als Projektverzeichnis oeffnen.
3. Passenden Skill aus `SKILLS.md` oder den Plugin-READMEs waehlen.
4. Fiktiven oder anonymisierten Sachverhalt eingeben.

Ausfuehrliche Installationsanleitung fuer Einsteigerinnen und Einsteiger:
`INSTALLATION_EINFACH.md`.

## Installation via Claude Code Marketplace

Die einfachste Methode: Marktplatz einmalig hinzufuegen, danach einzelne
Plugins installieren.

```
/plugin marketplace add markusbegerow/claude-fuer-oeffentliche-verwaltung
```

Anschliessend gewuenschte Plugins installieren (einzeln oder alle drei):

```
/plugin install verwaltung-digitalisierung-ki@verwaltung-skills
/plugin install verwaltung-fachverfahren-kommune@verwaltung-skills
/plugin install verwaltung-organisation-sicherheit@verwaltung-skills
```

Skills sind dann mit Plugin-Namen als Praefix aufrufbar, z. B.:

```
/verwaltung-digitalisierung-ki:ozg-umsetzung-pruefung
```

Updates beziehen:

```
/plugin marketplace update verwaltung-skills
```

## Regelwerk

Alle Skills folgen dem Regelwerk in `CLAUDE.md` (vollstaendig) und
`AGENTS.md` (Kurzfassung fuer andere Werkzeuge). Zentrale Bausteine:

- `references/zitierweise-verwaltung.md` — Quellenpflicht, keine
  Blindzitate.
- `references/methodik-verwaltungspruefung.md` — Pruefmethodik.
- `references/leitentscheidungen-verwaltung.md` — Themen-Anker zur
  Recherche.

## Rechtliche und tatsaechliche Risikohinweise

- **Schnelle Rechtsaenderung:** Verwaltungsdigitalisierung und die
  zugehoerigen Standards (OZG-Nachfolgeregelungen, IT-Planungsrat-
  Beschluesse, EU-KI-Verordnung) aendern sich fortlaufend. Jede Ausgabe
  nennt ein Stand-Datum.
- **Foederale Vielfalt:** Viele Themen (Wahlrecht, Kommunalverfassung,
  Haushaltsrecht) werden landesrechtlich unterschiedlich geregelt — jede
  Ausgabe weist auf zu pruefendes Landesrecht hin.
- **Keine operative Einsatztaktik:** Sicherheits- und blaulichtbezogene
  Skills vermitteln ausschliesslich organisatorische und kommunikative
  Ablaufhilfen, keine taktische Gefahrenabwehr.
- **Berufsrecht:** Die Nutzung der Skills entbindet nicht von den
  jeweiligen dienst- und berufsrechtlichen Sorgfaltspflichten.

## Lizenz

Apache-2.0 OR MIT — siehe `LICENSE`, `LICENSE-APACHE`, `LICENSE-MIT`.

## Weitere Dokumente

- `CONTRIBUTING.md` — Beitragsrichtlinien und PR-Checkliste.
- `CODE_OF_CONDUCT.md` — Verhaltenskodex.
- `CODEX.md` / `CODEX_INSTRUCTIONS_SKILL_VEREDELUNG.md` — Hinweise fuer
  andere LLM-Werkzeuge und zur Skill-Ueberarbeitung.
- `CONNECTORS.md` — Typische externe Datenquellen.
- `PROMPTLISTE.md` — Kuratierte Beispiel-Prompts.
- `EVAL_RESULTS.md` — Stand der Qualitaetsevaluation.
- `CHANGELOG.md` — Versionshistorie.
- `SKILLS.md` — Flacher Index aller Skills.

## 🙋‍♂️ Mitwirken

Bei Fragen oder Problemen:
- 🐛 [Fehler melden](https://github.com/markusbegerow/claude-fuer-oeffentliche-verwaltung/issues)
- 💡 [Feature vorschlagen](https://github.com/markusbegerow/claude-fuer-oeffentliche-verwaltung/issues)
- ⭐ Gerne einen Stern geben, wenn das Projekt nuetzlich ist!

## ☕ Projekt unterstuetzen

Wer das Projekt nuetzlich findet, kann die Weiterentwicklung mit einem
Repost oder einem Kaffee unterstuetzen:

<a href="https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/markusbegerow/claude-fuer-oeffentliche-verwaltung" target="_blank"> <img src="https://img.shields.io/badge/💼-Auf%20LinkedIn%20teilen-blue" /> </a>

[![Buy Me a Coffee](https://img.shields.io/badge/☕-Kaffee%20spendieren-yellow)](https://paypal.me/MarkusBegerow?country.x=DE&locale.x=de_DE)

## 📬 Kontakt

- 🧑‍💻 [Markus Begerow](https://linkedin.com/in/markusbegerow)
- 💾 [GitHub](https://github.com/markusbegerow)
- ✉️ [Twitter](https://x.com/markusbegerow)
