---
name: it-sicherheit-grundschutz-checkliste
description: "Checkliste der grundlegenden BSI-IT-Grundschutz-Anforderungen bei Einfuehrung eines neuen digitalen Verfahrens in einer Behoerde. Methodik Strukturanalyse und Schutzbedarfsfeststellung Abgleich mit einschlaegigen Bausteinen des IT-Grundschutz-Kompendiums Pruefung von Basisanforderungen zu Organisation Technik und Notfallvorsorge. Output ausformulierter Pruefbericht mit Schutzbedarfseinschaetzung und offenen Grundschutz-Massnahmen."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Checkliste der IT-Grundschutz-Anforderungen bei Einfuehrung eines digitalen Verfahrens

## Zweck / Anwendungsfall

Strukturierte Checkliste der grundlegenden Anforderungen des
BSI-IT-Grundschutzes, die bei der Einfuehrung eines neuen digitalen
Verfahrens (Fachanwendung, Online-Dienst, Schnittstelle) in einer Behoerde
zu beachten sind. Der Skill wird genutzt, wenn ein Fachbereich oder die
IT-Sicherheitsbeauftragte/der IT-Sicherheitsbeauftragte vor dem
Produktivbetrieb eines neuen Verfahrens pruefen moechte, welche
grundlegenden organisatorischen und technischen Schutzmassnahmen
vorgesehen oder bereits umgesetzt sind. Dieser Skill ersetzt keine
vollstaendige Grundschutz-Modellierung und keine Risikoanalyse durch die
zustaendige IT-Sicherheitsstelle.

## Eingaben

- Bezeichnung und kurze Beschreibung des neuen digitalen Verfahrens
  (Zweck, Nutzerkreis, Schnittstellen).
- Angabe der verarbeiteten Datenarten (allgemeine Verwaltungsdaten,
  personenbezogene Daten, besondere Kategorien personenbezogener Daten,
  Verschlusssachen-Bezug).
- Informationen zur Betriebsumgebung (eigenes Rechenzentrum, kommunaler
  IT-Dienstleister, Cloud-Dienst, On-Premise beim Fachverfahrenshersteller).
- Angabe, ob bereits eine Schutzbedarfsfeststellung oder eine
  Strukturanalyse fuer das Verfahren oder den IT-Verbund vorliegt.
- Angabe, ob das Verfahren an bestehende Netzinfrastruktur, Authentifizierung
  oder Protokollierung angebunden wird.

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: Verfahren, Betriebsumgebung und verarbeitete
   Datenarten strukturiert erfassen.
2. Strukturanalyse pruefen: welche IT-Systeme, Anwendungen, Raeume und
   Kommunikationsverbindungen sind am Verfahren beteiligt.
3. Schutzbedarfsfeststellung pruefen: Schutzbedarf hinsichtlich
   Vertraulichkeit, Integritaet und Verfuegbarkeit je Grundwert
   einschaetzen (normal, hoch, sehr hoch) und begruenden.
4. Einschlaegige Bausteine des IT-Grundschutz-Kompendiums identifizieren
   (z. B. zu IT-Betrieb, Anwendungen, Netzen, Organisation und Personal)
   und pruefen, ob die zugehoerigen Basis- und Standard-Anforderungen
   erfuellt sind (Edition/Stand des Kompendiums vor Verwendung
   verifizieren).
5. Organisatorische Basisanforderungen pruefen: Sicherheitskonzept,
   Verantwortlichkeiten, Schulung der Beschaeftigten, Berechtigungs-
   management.
6. Technische Basisanforderungen pruefen: Verschluesselung der
   Datenuebertragung, Authentifizierung, Protokollierung/Monitoring,
   Patch- und Update-Management, Schnittstellenabsicherung.
7. Notfallvorsorge pruefen: Datensicherung, Wiederanlaufplanung und
   Meldewege bei Sicherheitsvorfaellen (Bezug zu den Vorgaben fuer die
   Meldung von Sicherheitsvorfaellen an die zustaendige Stelle).
8. Schnittstelle zur datenschutzrechtlichen Pruefung benennen, insbesondere
   wenn personenbezogene Daten verarbeitet werden (Bezug zu Skill
   `datenschutz-folgenabschaetzung-pruefung`).
9. Offene Massnahmen und Risiken benennen, Prioritaeten vorschlagen.
10. Ergebnis mit Schutzbedarfseinschaetzung und offenen Massnahmen
    ausformulieren.

## Quellenpflicht

Verbindlich: `../../../references/zitierweise-verwaltung.md`. Keine
Blindzitate zu konkreten Baustein-Nummern, Editionsstaenden oder
Anforderungsbezeichnungen des IT-Grundschutz-Kompendiums — diese sind vom
Nutzer anhand der aktuellen Edition des BSI-IT-Grundschutz-Kompendiums zu
verifizieren oder als pruefungsbeduerftig zu kennzeichnen.

## Ausgabeformat

- Vollstaendig ausformulierte Pruefung im Pruefberichtsstil, kein reines
  Stichpunkt-Endergebnis.
- Tabellarische Checkliste je Grundschutz-Themenfeld (Organisation,
  Technik, Notfallvorsorge) mit Status "erfuellt/offen/zu pruefen" ist als
  ergaenzende Darstellung zulaessig.
- Stand-Datum angeben, inklusive Hinweis auf die zugrunde gelegte (vom
  Nutzer zu verifizierende) Edition des IT-Grundschutz-Kompendiums.
- Klar abgegrenztes Ergebnis am Ende ("Ergebnis: ...").
- Hinweis auf verbleibende Unsicherheiten.

## Beispiele

Beispiel (FIKTIV): Eine fiktive Landesbehoerde fuehrt ein neues
Online-Formularverfahren fuer Foerderantraege ein, das personenbezogene
Daten von Antragstellenden sowie Bankverbindungen verarbeitet und an ein
bestehendes Fachverfahren zur Foerdermittelverwaltung angebunden wird. Die
Pruefung ergibt einen Schutzbedarf "hoch" fuer Vertraulichkeit (Bankdaten)
und "normal" fuer Verfuegbarkeit. Es fehlen eine dokumentierte
Verschluesselung der Schnittstelle zum Fachverfahren und ein definierter
Meldeweg bei Sicherheitsvorfaellen. Empfehlung: Vor Produktivbetrieb
Transportverschluesselung und Authentifizierung der Schnittstelle
absichern, Meldeweg fuer Sicherheitsvorfaelle dokumentieren und mit der
IT-Sicherheitsbeauftragten/dem IT-Sicherheitsbeauftragten abstimmen.

## Normen und Standards

- BSI-Standards 200-1, 200-2 und 200-3 (IT-Grundschutz-Methodik,
  Risikoanalyse; Versionsstand vor Verwendung verifizieren).
- IT-Grundschutz-Kompendium des BSI (Edition/Stand vor Verwendung
  verifizieren).
- Gesetz ueber das Bundesamt fuer Sicherheit in der Informationstechnik
  (BSIG) sowie landesspezifische IT-Sicherheitsgesetze, soweit einschlaegig
  (Fundstelle vor Verwendung verifizieren).
- Allgemeine Datenschutz-Grundverordnung (DSGVO), insbesondere Art. 32
  zur Sicherheit der Verarbeitung.
- Onlinezugangsgesetz (OZG) hinsichtlich Sicherheitsanforderungen an
  digitale Verwaltungsleistungen.
