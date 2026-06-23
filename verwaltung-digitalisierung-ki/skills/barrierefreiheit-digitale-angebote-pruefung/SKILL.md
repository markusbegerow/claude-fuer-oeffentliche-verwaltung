---
name: barrierefreiheit-digitale-angebote-pruefung
description: "Pruefung eines digitalen Verwaltungsangebots auf Barrierefreiheit. Methodik Pruefung gegen BITV 2.0 BFSG und WCAG-Erfolgskriterien sowie Pruefung der Erklaerung zur Barrierefreiheit und des Feedback-Mechanismus. Output ausformulierter Pruefbericht mit Fundstellen je Kriterium und Mangelliste."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Pruefung der Barrierefreiheit eines digitalen Verwaltungsangebots

## Zweck / Anwendungsfall

Pruefung, ob ein digitales Verwaltungsangebot (Webseite, Portal,
mobile Anwendung) den Anforderungen der Barrierefreien-Informationstechnik-Verordnung
(BITV 2.0) beziehungsweise des Barrierefreiheitsstaerkungsgesetzes (BFSG)
sowie den einschlaegigen WCAG-Erfolgskriterien entspricht. Der Skill wird
genutzt, wenn eine Behoerde ein neues digitales Angebot vor Veroeffentlichung
pruefen oder ein bestehendes Angebot auf Nachbesserungsbedarf untersuchen
moechte.

## Eingaben

- URL oder Beschreibung des digitalen Angebots und seiner Hauptfunktionen.
- Angabe, ob bereits eine Erklaerung zur Barrierefreiheit veroeffentlicht
  ist und welchen Inhalt sie hat.
- Angabe zu eingesetzten Technologien (z. B. PDF-Formulare,
  JavaScript-Anwendung, Video-Inhalte).
- Ergebnisse vorhandener automatisierter oder manueller
  Barrierefreiheitspruefungen, falls vorhanden.
- Angabe, ob ein Feedback-Mechanismus fuer Nutzer mit
  Barrierefreiheitsproblemen existiert.

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: Angebot, Zielgruppe und eingesetzte
   Technologien erfassen.
2. Pruefen, ob eine Erklaerung zur Barrierefreiheit vorhanden ist und die
   vorgeschriebenen Inhalte (Konformitaetsstatus, Kontaktmoeglichkeit,
   Durchsetzungsverfahren) enthaelt.
3. Strukturelle Kriterien pruefen: semantische Auszeichnung, Tastaturbedienbarkeit,
   Kontraste, Textalternativen fuer Bilder.
4. Pruefen, ob PDF-Formulare und Dokumente barrierefrei aufbereitet sind
   (z. B. Tagging, Lesereihenfolge) oder durch zugaengliche HTML-Alternativen
   ergaenzt werden.
5. Pruefen, ob multimediale Inhalte (Video/Audio) Untertitel,
   Transkripte oder Audiodeskription bereitstellen, soweit erforderlich.
6. Feedback-Mechanismus pruefen: Erreichbarkeit, Reaktionszeiten,
   Eskalationsweg zur Durchsetzungs-/Überwachungsstelle.
7. Festgestellte Maengel nach WCAG-Erfolgskriterien kategorisieren und
   Priorisierung vorschlagen (kritisch, mittel, gering).
8. Ergebnis mit Mangelliste und empfohlenen naechsten Schritten
   ausformulieren.

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
- Hinweis auf verbleibende Unsicherheiten, insbesondere bei nicht manuell
  getesteten Inhalten.

## Beispiele

Beispiel (FIKTIV): Ein fiktives Buergerportal stellt einen Antrag
ausschliesslich als nicht getaggtes PDF-Formular ohne alternative
HTML-Eingabe bereit, eine Erklaerung zur Barrierefreiheit fehlt. Die
Pruefung ergibt erhebliche Maengel: fehlende Erklaerung zur
Barrierefreiheit, nicht barrierefreies PDF (keine Lesereihenfolge, keine
Alternativtexte), kein erkennbarer Feedback-Mechanismus. Empfehlung:
kurzfristige Veroeffentlichung einer Erklaerung zur Barrierefreiheit,
mittelfristige Umstellung auf ein barrierefrei getaggtes HTML-Formular,
Einrichtung eines Feedback-Kanals.

## Normen und Standards

- Barrierefreie-Informationstechnik-Verordnung (BITV 2.0), Versionsstand
  vor Verwendung verifizieren.
- Behindertengleichstellungsgesetz (BGG) als Rechtsgrundlage der BITV.
- Barrierefreiheitsstaerkungsgesetz (BFSG) fuer betroffene Produkte und
  Dienstleistungen, soweit einschlaegig.
- Web Content Accessibility Guidelines (WCAG), einschlaegige Version
  (z. B. WCAG 2.1/2.2) vor Verwendung verifizieren.
- EU-Richtlinie ueber den barrierefreien Zugang zu Websites und mobilen
  Anwendungen oeffentlicher Stellen (Richtlinie (EU) 2016/2102).
