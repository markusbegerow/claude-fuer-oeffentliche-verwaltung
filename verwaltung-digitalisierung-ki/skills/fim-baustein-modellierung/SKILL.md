---
name: fim-baustein-modellierung
description: "Modellierung eines Verwaltungsleistungs-Bausteins nach dem Foederalen Informationsmanagement (FIM). Methodik Erstellung von Leistungsbeschreibung Prozessbaustein und Datenfeldbaustein nach FIM-Standard. Output ausformulierter Modellierungsentwurf mit Hinweisen zu Wiederverwendung und Abstimmungsbedarf."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Modellierung eines FIM-Bausteins fuer eine Verwaltungsleistung

## Zweck / Anwendungsfall

Unterstuetzung bei der Modellierung eines Verwaltungsleistungs-Bausteins
nach der FIM-Methodik (Foederales Informationsmanagement), bestehend aus
Leistungsbeschreibung, Prozessbaustein und Datenfeldbaustein. Der Skill
wird genutzt, wenn eine Behoerde oder ein Fachverfahrenshersteller eine
Leistung erstmals strukturiert modellieren oder einen bestehenden Baustein
pruefen moechte.

## Eingaben

- Bezeichnung der Verwaltungsleistung und Rechtsgrundlage.
- Beschreibung des fachlichen Ablaufs (Antragstellung, Pruefung,
  Entscheidung, Bescheid) in Stichworten.
- Liste der Angaben, die der Antragsteller machen muss (Datenfelder).
- Angabe, ob bereits ein FIM-Baustein fuer eine vergleichbare Leistung in
  anderen Bundeslaendern/Kommunen existiert (Wiederverwendungspotenzial).
- Zielsystem/Fachverfahren, in dem der Baustein spaeter genutzt werden soll.

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: Rechtsgrundlage, Zustaendigkeit und fachlichen
   Ablauf der Leistung erfassen.
2. Pruefen, ob bereits ein FIM-Baustein im FIM-Portal/Baustein-Repository
   fuer eine identische oder vergleichbare Leistung existiert, der
   wiederverwendet oder adaptiert werden kann.
3. Leistungsbeschreibung entwerfen: Kurzbeschreibung, Zielgruppe,
   Voraussetzungen, Fristen, Kosten in einheitlicher FIM-Struktur.
4. Prozessbaustein entwerfen: Ablaufschritte von Antragstellung bis
   Bescheid, beteiligte Rollen, Entscheidungspunkte.
5. Datenfeldbaustein entwerfen: benoetigte Datenfelder, deren Typisierung
   und Wiederverwendbarkeit aus bestehenden FIM-Datenfeldbausteinen pruefen.
6. Konsistenz zwischen den drei Bausteinen pruefen (jedes im Prozess
   benoetigte Datenfeld muss im Datenfeldbaustein abgebildet sein).
7. Abstimmungsbedarf benennen (z. B. mit Land/Bund bei laenderuebergreifender
   Nutzung, mit Fachverfahrenshersteller bei technischer Umsetzung).
8. Ergebnis als Modellierungsentwurf mit offenen Punkten ausformulieren.

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

Beispiel (FIKTIV): Eine fiktive Gemeinde moechte einen FIM-Baustein fuer
die Leistung "Erteilung einer Sondernutzungserlaubnis fuer eine
Strassenkaffeeterrasse" modellieren. Es existiert noch kein vergleichbarer
Baustein im Repository. Die Pruefung entwirft eine Leistungsbeschreibung
mit Zielgruppe Gastronomiebetriebe, einen Prozessbaustein mit den Schritten
Antragstellung, Pruefung durch Ordnungsamt, Anhoerung Tiefbauamt,
Bescheiderteilung, sowie einen Datenfeldbaustein mit Feldern wie Standort,
Flaechengroesse und Nutzungszeitraum. Abstimmungsbedarf besteht mit dem
zustaendigen Land, falls der Baustein landesweit zur Wiederverwendung
vorgeschlagen werden soll.

## Normen und Standards

- FIM-Methodik des IT-Planungsrats (Leistungs-, Prozess- und
  Datenfeldbausteine), Versionsstand vor Verwendung verifizieren.
- Onlinezugangsgesetz (OZG) als uebergeordneter rechtlicher Rahmen.
- Einschlaegige Fachgesetze/Rechtsgrundlage der jeweiligen
  Verwaltungsleistung (im Einzelfall zu bestimmen).
- IT-Planungsrat-Beschluesse zur Pflege und Bereitstellung von
  FIM-Bausteinen (Beschlussnummer vor Verwendung verifizieren).
