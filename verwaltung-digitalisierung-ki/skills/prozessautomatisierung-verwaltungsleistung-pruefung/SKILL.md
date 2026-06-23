---
name: prozessautomatisierung-verwaltungsleistung-pruefung
description: "Pruefung der Eignung einer Verwaltungsleistung fuer eine vollstaendige oder teilweise Automatisierung von Bearbeitungsschritten. Methodik Analyse der Bearbeitungsschritte Identifikation regelbasierter Entscheidungen Eignung fuer Workflow-Engine oder Schnittstellen zu Fachverfahren Abgrenzung automatisierbarer und entscheidungsbeduerftiger Schritte. Output ausformulierter Pruefbericht mit Automatisierungsgrad je Bearbeitungsschritt und Empfehlung zum weiteren Vorgehen."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Pruefung der Automatisierungseignung einer Verwaltungsleistung

## Zweck / Anwendungsfall

Pruefung, ob und in welchem Umfang die Bearbeitungsschritte einer
konkreten Verwaltungsleistung fuer eine (Teil-)Automatisierung geeignet
sind. Der Skill wird genutzt, wenn eine Behoerde oder ein IT-Dienstleister
vor der Einfuehrung einer Workflow-Engine, einer regelbasierten
Entscheidungsunterstuetzung oder einer automatisierten Schnittstelle zu
einem Fachverfahren systematisch klaeren moechte, welche Schritte sich
automatisieren lassen und welche zwingend eine menschliche Bearbeitung
erfordern.

## Eingaben

- Bezeichnung der Verwaltungsleistung und zustaendige Behoerde/Ebene.
- Beschreibung des aktuellen Bearbeitungsprozesses, moeglichst als
  Schrittfolge (Eingang, Pruefung, Entscheidung, Bescheid, Versand).
- Angabe, welche Pruefschritte auf klar definierten, in Rechtsnormen oder
  Verwaltungsvorschriften festgelegten Kriterien beruhen (regelbasiert)
  und welche Ermessen oder Wertung erfordern.
- Informationen zu vorhandenen Fachverfahren und deren Schnittstellen
  (API, Dateiexport, manuelle Erfassung).
- Angabe, ob bereits eine Workflow-Engine oder ein
  Vorgangsbearbeitungssystem im Einsatz ist.
- Fallzahlen/Bearbeitungsvolumen, soweit fuer die Wirtschaftlichkeit der
  Automatisierung relevant.

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: Verwaltungsleistung, Prozessschritte und
   beteiligte Fachverfahren strukturiert erfassen.
2. Jeden Bearbeitungsschritt einzeln klassifizieren: vollstaendig
   regelbasiert (automatisierbar), teilweise regelbasiert (Vorpruefung
   automatisierbar, Entscheidung verbleibt beim Menschen) oder
   ermessens-/wertungsabhaengig (nicht automatisierbar).
3. Pruefen, ob fuer regelbasierte Schritte eine eindeutige, dokumentierte
   Rechtsgrundlage besteht, aus der sich die Entscheidungsregeln ableiten
   lassen (Voraussetzung fuer eine regelbasierte Engine).
4. Pruefen, ob und wie eine Workflow-Engine die Prozessschritte technisch
   abbilden kann (Verzweigungen, Fristen, Eskalationen, Wiedervorlagen).
5. Schnittstellenbedarf zu Fachverfahren pruefen: welche Daten muessen
   automatisiert ausgetauscht werden, welche Schnittstellenstandards
   (siehe Skill `interoperabilitaet-datenaustausch-pruefung`) kommen in
   Betracht.
6. Pruefen, ob fuer automatisierte Entscheidungsschritte zusaetzliche
   Anforderungen gelten (Begruendungspflicht, Dokumentationspflicht,
   Widerspruchsrecht bei vollautomatisierten Verwaltungsakten, Bezug zu
   Skill `ki-einsatz-verwaltungsverfahren-pruefung`, falls KI-Komponenten
   beteiligt sind).
7. Risiken und Grenzen der Automatisierung benennen (Fehleranfaelligkeit
   bei Sonderfaellen, Akzeptanz bei Mitarbeitenden und Antragstellenden,
   Wartungsaufwand der Regeln bei Rechtsaenderungen).
8. Ergebnis mit Automatisierungsgrad je Schritt und priorisierter
   Empfehlung ausformulieren.

## Quellenpflicht

Verbindlich: `../../../references/zitierweise-verwaltung.md`. Keine
Blindzitate zu Beschlussnummern, Versionsstaenden oder Paragrafen — diese
sind vom Nutzer zu verifizieren oder als pruefungsbeduerftig zu
kennzeichnen.

## Ausgabeformat

- Vollstaendig ausformulierte Pruefung im Pruefberichtsstil, kein reines
  Stichpunkt-Endergebnis.
- Tabellarische Uebersicht der Bearbeitungsschritte mit
  Automatisierungsgrad ist als ergaenzende Darstellung zulaessig.
- Stand-Datum angeben.
- Klar abgegrenztes Ergebnis am Ende ("Ergebnis: ...").
- Hinweis auf verbleibende Unsicherheiten.

## Beispiele

Beispiel (FIKTIV): Eine fiktive Kommune "Musterstadt" prueft die
Verwaltungsleistung "Erteilung eines Parkausweises fuer Anwohner". Der
Prozess umfasst Antragseingang, Pruefung der Meldeadresse, Pruefung des
Fahrzeugscheins, Gebuehrenberechnung und Ausstellung des Ausweises. Die
Pruefung ergibt: Antragseingang und Pruefung der Meldeadresse sind
regelbasiert automatisierbar (Abgleich mit dem Melderegister, vgl. Skill
`registermodernisierung-once-only-pruefung`), die Gebuehrenberechnung ist
vollstaendig regelbasiert automatisierbar, die Pruefung des
Fahrzeugscheins erfordert derzeit eine manuelle Sichtpruefung mangels
strukturierter Schnittstelle zum Fahrzeugregister. Empfehlung:
Teilautomatisierung mit Workflow-Engine fuer Antragseingang, Melderegister-
abgleich und Gebuehrenberechnung, manuelle Pruefung des Fahrzeugscheins
bleibt vorerst erhalten.

## Normen und Standards

- Verwaltungsverfahrensgesetz (VwVfG), insbesondere Vorschriften zum
  vollautomatisierten Erlass von Verwaltungsakten (Fundstelle vor
  Verwendung verifizieren).
- Onlinezugangsgesetz (OZG) und OZG-Nachfolgeregelungen hinsichtlich
  durchgaengig digitaler Bearbeitung.
- FIM-Prozessbausteine des IT-Planungsrats als Grundlage fuer die
  Prozessmodellierung.
- Einschlaegige Fachgesetze der jeweiligen Verwaltungsleistung
  (Versionsstand vor Verwendung verifizieren).
