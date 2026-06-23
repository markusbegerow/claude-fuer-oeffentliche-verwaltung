---
name: ozg-umsetzung-pruefung
description: "Pruefung des Umsetzungsstands einer Verwaltungsleistung nach dem Onlinezugangsgesetz (OZG). Methodik Leistungsbeschreibung Once-Only-Faehigkeit Nutzerkontoanbindung Antragsdatenmodell medienbruchfreie Bearbeitung. Output ausformulierter Pruefbericht mit Reifegrad je Pruefkriterium und Hinweis auf offene Umsetzungsschritte."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Pruefung des OZG-Umsetzungsstands einer Verwaltungsleistung

## Zweck / Anwendungsfall

Pruefung, wie weit eine konkrete Verwaltungsleistung die Anforderungen des
Onlinezugangsgesetzes (OZG) und seiner Nachfolgeregelungen bereits umsetzt.
Der Skill wird genutzt, wenn eine Behoerde oder ein IT-Dienstleister den
Digitalisierungsstand eines Antrags- oder Genehmigungsverfahrens bewerten
und naechste Umsetzungsschritte ableiten moechte.

## Eingaben

- Bezeichnung der Verwaltungsleistung und zustaendige Behoerde/Ebene
  (Bund, Land, Kommune).
- Beschreibung des aktuellen Antragswegs (papierbasiert, Online-Formular,
  Volldigitalisierung).
- Angabe, ob und wie ein Nutzerkonto (BundID, Unternehmenskonto, laenderspezifisches
  Servicekonto) eingebunden ist.
- Angabe, ob bereits vorhandene Daten aus Registern automatisiert
  einbezogen werden (Once-Only-Ansatz) oder der Nutzer Angaben erneut
  erfassen muss.
- Informationen zur Schnittstelle des Fachverfahrens (Anbindung an
  Backend-Systeme, manuelle Medienbrueche).

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: Verwaltungsleistung, Zustaendigkeit und
   bisherigen Digitalisierungsstand strukturiert erfassen.
2. Einordnen, welchem OZG-Leistungsbuendel/Lebenslage die Leistung
   zugeordnet ist und ob bereits eine FIM-Leistungsbeschreibung existiert.
3. Pruefen, ob ein medienbruchfreier digitaler Zugang besteht (Formular,
   Identifizierung, Bezahlung, Bescheidzustellung) oder an welcher Stelle
   ein Medienbruch (Druck, Fax, manuelle Uebertragung) vorliegt.
4. Pruefen, ob die Nutzerkontoanbindung (BundID/Unternehmenskonto) korrekt
   eingebunden ist und welches Vertrauensniveau gefordert wird (siehe Skill
   `digitale-identitaet-nutzerkonto-auswahl`).
5. Pruefen, ob das Antragsdatenmodell einem FIM-Datenfeldbaustein folgt
   oder leistungsspezifisch frei definiert ist.
6. Once-Only-Faehigkeit pruefen: welche Angaben koennten technisch bereits
   aus Registern bezogen werden, geschieht dies tatsaechlich (siehe Skill
   `registermodernisierung-once-only-pruefung`).
7. Offene Umsetzungsschritte und Risiken benennen (z. B. fehlende
   FIT-Connect-Anbindung, fehlende Barrierefreiheitspruefung).
8. Ergebnis mit Reifegradeinschaetzung ausformulieren.

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

Beispiel (FIKTIV): Eine fiktive Kommune "Musterstadt" bietet die
Verwaltungsleistung "Anmeldung eines Gewerbes" aktuell als PDF-Formular
zum Download an, das ausgedruckt und persoenlich oder per Post eingereicht
werden muss. Es besteht keine Anbindung an ein Nutzerkonto und keine
automatisierte Datenuebernahme aus dem Gewerberegister. Die Pruefung
ergibt: Reifegrad niedrig (Formular online verfuegbar, aber kein
medienbruchfreier digitaler Zugang, keine Once-Only-Faehigkeit, keine
Nutzerkontoanbindung). Empfohlene naechste Schritte: FIM-Leistungsbaustein
"Gewerbeanmeldung" pruefen, BundID-Anbindung vorbereiten, Anbindung an
FIT-Connect fuer die Antragsuebermittlung an das Fachverfahren planen.

## Normen und Standards

- Onlinezugangsgesetz (OZG) und OZG-Aenderungsgesetz/Nachfolgeregelungen
  (Fundstelle/Versionsstand vor Verwendung verifizieren).
- IT-Planungsrat-Beschluesse zu OZG-Umsetzung und Priorisierung
  (Beschlussnummer vor Verwendung verifizieren).
- FIM-Methodik (Leistungs-, Prozess- und Datenfeldbausteine) des IT-Planungsrats.
- Servicestandard des Bundes fuer digitale Verwaltungsleistungen.
