---
name: interoperabilitaet-datenaustausch-pruefung
description: "Pruefung der technischen und semantischen Interoperabilitaet eines Datenaustauschs zwischen Behoerden. Methodik Pruefung von Schnittstellenform XOEV-Standardnutzung Datenmodell und Versionskompatibilitaet. Output ausformulierte Einordnung mit Empfehlung zu Standardisierung und offenen Anpassungsbedarfen."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Pruefung der Interoperabilitaet eines behoerdlichen Datenaustauschs

## Zweck / Anwendungsfall

Pruefung der technischen und semantischen Interoperabilitaet eines
Datenaustauschs zwischen zwei oder mehr Behoerden oder Fachverfahren. Der
Skill wird genutzt, wenn eine Schnittstelle neu konzipiert oder eine
bestehende Schnittstelle auf Standardkonformitaet (insbesondere
XOEV-Standards) und Zukunftsfaehigkeit ueberprueft werden soll.

## Eingaben

- Beteiligte Systeme/Behoerden und Zweck des Datenaustauschs.
- Aktuelles oder geplantes Datenformat/Schema des Austauschs.
- Angabe, ob ein XOEV-Standard (z. B. ein fachspezifischer XOEV-Standard)
  fuer den Anwendungsfall existiert und genutzt wird.
- Informationen zur Versionierung und Aenderungsverwaltung der Schnittstelle.
- Angabe zur Transportebene (z. B. FIT-Connect, Webservice, Dateiaustausch).

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: beteiligte Systeme, Datenflussrichtung und
   fachlichen Zweck des Austauschs erfassen.
2. Technische Interoperabilitaet pruefen: einheitliche Transportprotokolle,
   Schnittstellenform (synchron/asynchron), Verfuegbarkeit einer
   maschinenlesbaren Schemadefinition.
3. Semantische Interoperabilitaet pruefen: einheitliche Bedeutung und
   Typisierung der ausgetauschten Datenfelder, Vermeidung von
   Mehrfachdefinitionen gleicher Sachverhalte.
4. Pruefen, ob ein passender XOEV-Standard existiert und angewendet wird,
   oder ob eine Standardisierungsluecke besteht.
5. Versionskompatibilitaet pruefen: wie werden Schemaaenderungen
   kommuniziert und rueckwaertskompatibel gehalten.
6. Pruefen, ob der Datenaustausch FIM-Datenfeldbausteine wiederverwendet
   (siehe Skill `fim-baustein-modellierung`) oder eigene, parallele
   Datenmodelle entstehen.
7. Organisatorische Abhaengigkeiten benennen (Pflegegremium des Standards,
   Mitwirkungspflichten der beteiligten Behoerden).
8. Ergebnis mit Empfehlung zur Standardisierung ausformulieren.

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

Beispiel (FIKTIV): Zwei fiktive Fachverfahren unterschiedlicher Behoerden
sollen Daten zu einer gemeinsamen Fallbearbeitung austauschen. Aktuell
existiert ein proprietaeres CSV-Format ohne formale Schemadefinition. Die
Pruefung ergibt eine geringe technische und semantische Interoperabilitaet,
da Feldbedeutungen nicht eindeutig dokumentiert sind und keine
Versionsverwaltung existiert. Empfehlung: Pruefung, ob ein passender
XOEV-Standard existiert oder ein FIM-Datenfeldbaustein als gemeinsame
Grundlage definiert werden kann, sowie Einfuehrung einer formalen
Schemavalidierung vor produktivem Einsatz.

## Normen und Standards

- XOEV-Rahmenwerk (XOEV-Handbuch) fuer die Entwicklung von
  Datenaustauschstandards, Versionsstand vor Verwendung verifizieren.
- FIM-Methodik des IT-Planungsrats fuer Datenfeldbausteine.
- IT-Planungsrat-Beschluesse zur Interoperabilitaet und gemeinsamen
  Standards (Beschlussnummer vor Verwendung verifizieren).
- Onlinezugangsgesetz (OZG) und Registermodernisierungsgesetz als
  rechtlicher Rahmen fuer den behoerdenuebergreifenden Datenaustausch.
