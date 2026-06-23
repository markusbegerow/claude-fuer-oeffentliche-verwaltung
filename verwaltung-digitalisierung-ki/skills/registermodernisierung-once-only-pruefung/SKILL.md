---
name: registermodernisierung-once-only-pruefung
description: "Pruefung eines Datenaustauschs zwischen Behoerden auf Vereinbarkeit mit dem Once-Only-Prinzip nach dem Registermodernisierungsgesetz. Methodik Pruefung von Identifikationsmerkmal Registerbasis Einwilligung und Datenschutzkonformitaet. Output ausformulierte Einordnung mit Ergebnis zur Once-Only-Faehigkeit."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Pruefung der Once-Only-Faehigkeit nach dem Registermodernisierungsgesetz

## Zweck / Anwendungsfall

Pruefung, ob ein konkreter Datenaustausch zwischen Behoerden dem
Once-Only-Prinzip (Bereitstellung bereits vorhandener Daten aus
Registern, statt erneuter Erfassung durch den Buerger) im Sinne des
Registermodernisierungsgesetzes entspricht. Der Skill wird genutzt, wenn
eine Behoerde pruefen moechte, ob und wie eine Datenabfrage aus einem
anderen Register zulaessig automatisiert erfolgen kann.

## Eingaben

- Bezeichnung der beteiligten Register (abgebende und empfangende
  Behoerde/Register).
- Art der auszutauschenden Daten und deren Zweckbindung im
  Ausgangsverfahren.
- Angabe, ob eine Einwilligung des Betroffenen vorgesehen ist oder eine
  gesetzliche Ermaechtigung den Austausch ohne Einzeleinwilligung erlaubt.
- Angabe zum verwendeten oder geplanten Identifikationsmerkmal fuer die
  eindeutige Zuordnung (z. B. registeruebergreifende Identifikationsnummer).
- Technische Schnittstelle des abgebenden Registers (vorhanden,
  geplant, nicht vorhanden).

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: beteiligte Register, Datenarten und
   Verwendungszweck erfassen.
2. Pruefen, ob fuer den Datenaustausch eine gesetzliche Ermaechtigung nach
   dem Registermodernisierungsgesetz oder einem Fachgesetz vorliegt.
3. Pruefen, ob ein geeignetes Identifikationsmerkmal fuer die
   registeruebergreifende Zuordnung vorgesehen und datenschutzrechtlich
   zulaessig genutzt wird.
4. Pruefen, ob eine informierte Einwilligung des Betroffenen erforderlich
   ist und wie diese im Antragsprozess eingeholt wird.
5. Pruefen, ob die abgebende Stelle technisch in der Lage ist, die Daten
   strukturiert (z. B. ueber eine standardisierte Schnittstelle)
   bereitzustellen.
6. Datenschutzrechtliche Aspekte pruefen (Zweckbindung,
   Verhaeltnismaessigkeit, Protokollierungspflichten der Abfrage).
7. Restliche Medienbrueche benennen, falls der Once-Only-Ansatz nur
   teilweise umsetzbar ist.
8. Ergebnis mit Einordnung zur Once-Only-Faehigkeit ausformulieren.

## Quellenpflicht

Verbindlich: `../../../references/zitierweise-verwaltung.md`. Keine
Blindzitate zu Beschlussnummern, Versionsstaenden oder Paragrafen — diese
sind vom Nutzer zu verifizieren oder als pruefungsbeduerftig zu
kennzeichnen.

## Ausgabeformat

- Vollstaendig ausformulierte Pruefung im Pruefberichtsstil, kein reines
  Stichpunkt-Endergebnis.
- Stand-Datum angeben.
- Klar abgegrenztes Ergebnis am Ende ("Ergebnis: ...").
- Hinweis auf verbleibende Unsicherheiten.

## Beispiele

Beispiel (FIKTIV): Bei einem fiktiven Antrag auf Elterngeld soll die
Meldebehoerde automatisiert bestaetigen, dass der Antragsteller an der
angegebenen Adresse gemeldet ist, anstatt dass der Antragsteller eine
Meldebescheinigung beibringen muss. Die Pruefung ergibt: eine gesetzliche
Ermaechtigung fuer den Datenabruf liegt grundsaetzlich vor, eine informierte
Einwilligung wird im Antragsprozess eingeholt, die technische Schnittstelle
zur Meldebehoerde ist jedoch noch nicht produktiv. Ergebnis: Once-Only-Faehigkeit
ist rechtlich angelegt, aber technisch noch nicht vollstaendig umgesetzt;
bis zur Inbetriebnahme bleibt eine manuelle Nachweisfuehrung erforderlich.

## Normen und Standards

- Gesetz zur Verbesserung der Verwaltungsleistungen durch Verbesserung des
  Datenaustauschs (Registermodernisierungsgesetz), Versionsstand vor
  Verwendung verifizieren.
- Allgemeine Datenschutz-Grundverordnung (DSGVO), insbesondere
  Grundsaetze der Zweckbindung und Datenminimierung.
- Onlinezugangsgesetz (OZG) als uebergeordneter Rahmen fuer die
  Antragsdigitalisierung.
- IT-Planungsrat-Beschluesse zur Umsetzung des Once-Only-Prinzips
  (Beschlussnummer vor Verwendung verifizieren).
