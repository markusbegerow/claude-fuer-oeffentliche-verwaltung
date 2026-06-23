---
name: datenschutz-folgenabschaetzung-pruefung
description: "Pruefung ob fuer ein Verfahren eine Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO erforderlich ist und welche Schritte sie umfasst. Methodik Pruefung der Risikoindikatoren fuer ein hohes Risiko Abgleich mit Positivlisten der Aufsichtsbehoerden Pruefung des Ablaufs einer Folgenabschaetzung samt Risikobewertung und Massnahmen. Output ausformulierter Pruefbericht mit Erforderlichkeitseinschaetzung und Vorschlag fuer das weitere Vorgehen."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Pruefung der Erforderlichkeit einer Datenschutz-Folgenabschaetzung

## Zweck / Anwendungsfall

Pruefung, ob fuer ein konkretes Verfahren der Verarbeitung
personenbezogener Daten eine Datenschutz-Folgenabschaetzung (DSFA) nach
Art. 35 der Datenschutz-Grundverordnung (DSGVO) erforderlich ist, und
falls ja, welche Schritte eine solche Folgenabschaetzung umfasst. Der
Skill wird genutzt, wenn eine Behoerde ein neues digitales Verfahren, ein
neues Fachverfahren oder eine neue Datenverarbeitung einfuehrt und vorab
klaeren moechte, ob die gesetzliche Schwelle fuer eine DSFA erreicht ist.
Dieser Skill ersetzt keine Abstimmung mit der/dem behoerdlichen
Datenschutzbeauftragten und keine eigenstaendige Durchfuehrung der DSFA.

## Eingaben

- Beschreibung des Verfahrens und des Verarbeitungszwecks
  (Verwaltungsleistung, Fachverfahren, Datenaustausch).
- Art und Umfang der verarbeiteten personenbezogenen Daten, insbesondere
  Angabe, ob besondere Kategorien personenbezogener Daten (Art. 9 DSGVO)
  oder Daten ueber strafrechtliche Verurteilungen betroffen sind.
- Angabe der betroffenen Personengruppen und der ungefaehren Anzahl
  betroffener Personen.
- Angabe, ob automatisierte Entscheidungsfindung, systematische
  Beobachtung, Profiling oder eine neue Technologie (z. B. KI-Einsatz,
  biometrische Verfahren) zum Einsatz kommt.
- Informationen zu bereits vorhandenen Risikoeinschaetzungen oder einem
  Verzeichnis von Verarbeitungstaetigkeiten fuer das Verfahren.

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: Verfahren, Verarbeitungszweck, Datenarten und
   betroffene Personengruppen strukturiert erfassen.
2. Pruefen, ob eines der gesetzlichen Regelbeispiele des Art. 35 Abs. 3
   DSGVO einschlaegig ist (u. a. systematische und umfassende Bewertung
   natuerlicher Personen mit Rechtswirkung, umfangreiche Verarbeitung
   besonderer Kategorien personenbezogener Daten, systematische
   weiteraeumige Ueberwachung oeffentlich zugaenglicher Bereiche).
3. Pruefen, ob die Verarbeitung in einer "Muss"- oder "Positivliste" der
   zustaendigen Datenschutzaufsichtsbehoerde (Liste der Verarbeitungs-
   vorgaenge, fuer die eine DSFA durchzufuehren ist) aufgefuehrt ist, oder
   ob eine einschlaegige "Negativliste" eine Ausnahme vorsieht (Fundstelle
   und Aktualitaet der jeweiligen Liste vor Verwendung verifizieren).
4. Allgemeine Risikoindikatoren der Aufsichtsbehoerden pruefen (z. B.
   Bewertung/Scoring, automatisierte Entscheidungsfindung mit
   Rechtswirkung, systematische Ueberwachung, sensible Daten,
   Datenverarbeitung in grossem Umfang, Zusammenfuehrung von
   Datensaetzen, Daten ueber schutzbeduerftige Betroffene, innovative
   Nutzung neuer Technologien).
5. Bei Erforderlichkeit einer DSFA den vorgesehenen Ablauf skizzieren:
   systematische Beschreibung der Verarbeitung, Bewertung der
   Notwendigkeit und Verhaeltnismaessigkeit, Risikobewertung fuer die
   Rechte und Freiheiten der betroffenen Personen, vorgesehene Massnahmen
   zur Risikobewaeltigung.
6. Pruefen, ob bei verbleibendem hohem Risiko trotz Massnahmen eine
   vorherige Konsultation der Aufsichtsbehoerde nach Art. 36 DSGVO in
   Betracht kommt.
7. Schnittstelle zu weiteren Pruefungen benennen (z. B.
   IT-sicherheitsrechtliche Pruefung nach Skill
   `it-sicherheit-grundschutz-checkliste`, KI-bezogene Pruefung nach Skill
   `ki-einsatz-verwaltungsverfahren-pruefung`).
8. Ergebnis mit Erforderlichkeitseinschaetzung und Vorschlag fuer das
   weitere Vorgehen ausformulieren.

## Quellenpflicht

Verbindlich: `../../../references/zitierweise-verwaltung.md`. Keine
Blindzitate zu konkreten Positivlisten-Eintraegen, Beschlussnummern oder
Versionsstaenden — diese sind vom Nutzer anhand der aktuellen Positivliste
der zustaendigen Aufsichtsbehoerde zu verifizieren oder als
pruefungsbeduerftig zu kennzeichnen.

## Ausgabeformat

- Vollstaendig ausformulierte Pruefung im Pruefberichtsstil, kein reines
  Stichpunkt-Endergebnis.
- Stand-Datum angeben.
- Klar abgegrenztes Ergebnis am Ende ("Ergebnis: ..."), das ausdruecklich
  benennt, ob eine DSFA erforderlich, voraussichtlich erforderlich,
  voraussichtlich nicht erforderlich oder im Einzelfall mit der/dem
  Datenschutzbeauftragten zu klaeren ist.
- Hinweis auf verbleibende Unsicherheiten und auf die Pflicht zur
  Abstimmung mit der/dem behoerdlichen Datenschutzbeauftragten.

## Beispiele

Beispiel (FIKTIV): Eine fiktive Behoerde plant die Einfuehrung eines
Systems zur automatisierten Vorpruefung und Risikobewertung von
Sozialleistungsantraegen, das fuer jeden Antrag einen Risikoscore berechnet
und bei hohem Score eine vertiefte manuelle Pruefung auslaesst. Die
Pruefung ergibt: Es liegt eine systematische und umfassende Bewertung
natuerlicher Personen mit potenzieller Rechtswirkung vor (Regelbeispiel
Art. 35 Abs. 3 DSGVO), zudem werden voraussichtlich besondere Kategorien
personenbezogener Daten verarbeitet. Ergebnis: Eine Datenschutz-
Folgenabschaetzung ist voraussichtlich erforderlich. Empfehlung: Vor
Produktivbetrieb DSFA mit der/dem behoerdlichen Datenschutzbeauftragten
durchfuehren, Risikobewertung insbesondere zur Erklaerbarkeit des
Scoring-Modells und zu Diskriminierungsrisiken dokumentieren.

## Normen und Standards

- Verordnung (EU) 2016/679 (Datenschutz-Grundverordnung, DSGVO),
  insbesondere Art. 35 (Datenschutz-Folgenabschaetzung) und Art. 36
  (vorherige Konsultation).
- Positivlisten und Leitlinien der zustaendigen Datenschutzaufsichts-
  behoerden zur Pflicht einer DSFA (Fundstelle und Aktualitaet vor
  Verwendung verifizieren).
- Bundesdatenschutzgesetz (BDSG) sowie landesspezifische
  Datenschutzgesetze, soweit einschlaegig (Fundstelle vor Verwendung
  verifizieren).
- Verordnung (EU) 2024/1689 (KI-Verordnung/AI Act) hinsichtlich des
  Verhaeltnisses zwischen Grundrechte-Folgenabschaetzung und DSFA, soweit
  ein KI-System beteiligt ist.
