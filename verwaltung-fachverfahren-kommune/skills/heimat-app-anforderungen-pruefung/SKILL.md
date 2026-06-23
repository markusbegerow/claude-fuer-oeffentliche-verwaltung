---
name: heimat-app-anforderungen-pruefung
description: "Prueft fachliche und technische Anforderungen an eine kommunale Heimat-App hinsichtlich Funktionsumfang Datenschutz und Barrierefreiheit. Methodik Sachverhaltsaufbereitung Einordnung Anforderungen Umsetzungsschritte Ergebnis. Output ausformulierte Pruefung mit Ergebnis zur Anforderungserfuellung."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Pruefung der Anforderungen an eine kommunale Heimat-App

## Zweck / Anwendungsfall

Pruefung der fachlichen und technischen Anforderungen an eine kommunale
"Heimat-App" (App fuer Buergerinnen und Buerger mit lokalen
Informationen, Veranstaltungen, Meldefunktionen und ggf. Verwaltungs-
Schnittstellen), insbesondere hinsichtlich Funktionsumfang, Datenschutz
und Barrierefreiheit. Dieser Skill wird genutzt, wenn eine Kommune die
Einfuehrung oder Weiterentwicklung einer solchen App strukturiert pruefen
moechte, etwa vor einer Beschaffungsentscheidung oder vor dem Abschluss
eines Pflichtenhefts.

## Eingaben

- Geplanter Funktionsumfang (z. B. Veranstaltungskalender, Maengelmelder,
  Push-Benachrichtigungen, Anbindung an Buergerportal/Fachverfahren).
- Zielgruppen und erwartete Nutzendenzahl.
- Angaben zum Anbieter/Betreibermodell (Eigenentwicklung, Beschaffung
  einer Standardloesung, Auftragsverarbeitung durch Dritte).
- Angaben zu erhobenen und verarbeiteten personenbezogenen Daten.
- Angaben zur Hosting-Umgebung (z. B. kommunales Rechenzentrum, externer
  Cloud-Anbieter, Serverstandort).
- Angaben zu vorgesehenen Barrierefreiheits-Massnahmen.

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: Funktionsumfang, Zielgruppen und
   Betreibermodell der App dokumentieren.
2. Einordnen, ob die App als reines Informationsangebot, als
   interaktives Beteiligungsinstrument (z. B. Maengelmelder) oder als
   Zugang zu Verwaltungsleistungen (mit Authentifizierung) konzipiert
   ist, da sich daraus unterschiedliche rechtliche Anforderungen
   ergeben.
3. Funktionsumfang gegen den beabsichtigten Nutzen pruefen: Redundanzen
   zu bestehenden Angeboten (z. B. bereits vorhandenes Buergerportal)
   identifizieren.
4. Datenschutzrechtliche Grundpruefung vornehmen: Rechtsgrundlage der
   Datenverarbeitung, Auftragsverarbeitungsvertrag bei externem
   Anbieter, Serverstandort, Loeschkonzept, Informationspflichten nach
   der DSGVO.
5. IT-Sicherheitsrechtliche Grundpruefung vornehmen: Authentifizierung,
   Verschluesselung der Datenuebertragung, Update- und
   Patch-Management, Schnittstellen zu Fachverfahren.
6. Barrierefreiheit pruefen: Konformitaet mit den Vorgaben zur digitalen
   Barrierefreiheit (z. B. Bedienbarkeit fuer Screenreader, ausreichende
   Kontraste, verstaendliche Sprache), insbesondere wenn die App
   oeffentliche Stellen betrifft.
7. Pruefen, ob ein Beteiligungsprozess mit relevanten Gremien (z. B.
   Datenschutzbeauftragte, IT-Sicherheitsbeauftragte, Gleichstellungs-
   oder Behindertenbeauftragte der Kommune) vorgesehen ist.
8. Ergebnis formulieren: Erfuellungsgrad der fachlichen und technischen
   Anforderungen, identifizierte Luecken, priorisierte
   Handlungsempfehlungen.

## Quellenpflicht

Verbindlich: `../../../references/zitierweise-verwaltung.md`. Keine
Blindzitate zu Paragrafen, Fristen oder Aktenzeichen — diese sind vom
Nutzer zu verifizieren oder als pruefungsbeduerftig zu kennzeichnen.

## Ausgabeformat

- Vollstaendig ausformulierte Pruefung im Pruefberichtsstil, kein reines
  Stichpunkt-Endergebnis.
- Stand-Datum angeben.
- Klar abgegrenztes Ergebnis am Ende ("Ergebnis: ...").
- Hinweis auf verbleibende Unsicherheiten.

## Beispiele

Beispiel (FIKTIV): Eine fiktive Kommune plant eine Heimat-App mit
Veranstaltungskalender, Maengelmelder und Push-Benachrichtigungen, die
von einem externen Anbieter mit Hosting in einem Drittland betrieben
werden soll. Ein Auftragsverarbeitungsvertrag liegt als Entwurf vor, ein
Loeschkonzept fehlt bislang. Ergebnis (fiktiv): Der Funktionsumfang
erscheint fachlich nachvollziehbar; aus Datenschutzsicht bestehen jedoch
offene Punkte, insbesondere zum Drittlandbezug des Hostings und zum
fehlenden Loeschkonzept, die vor einer Beschaffungsentscheidung mit der
zustaendigen Datenschutzbeauftragten zu klaeren sind.

## Normen und Standards

- Datenschutz-Grundverordnung (DSGVO), insbesondere zu Rechtsgrundlagen
  der Verarbeitung, Auftragsverarbeitung und Drittlandtransfers
  (Fundstelle vor Verwendung verifizieren).
- Bundesdatenschutzgesetz (BDSG) und ggf. Landesdatenschutzgesetz des
  betroffenen Bundeslandes.
- Barrierefreie-Informationstechnik-Verordnung (BITV) bzw. die
  entsprechende Landesverordnung zur digitalen Barrierefreiheit.
- IT-Sicherheitsstandards (z. B. BSI-Grundschutz), soweit von der
  Kommune oder dem zustaendigen IT-Dienstleister angewendet.
- Hinweis: Zustaendigkeiten und ergaenzende Vorgaben koennen je
  Bundesland und Kommune variieren — das jeweils einschlaegige
  Landesrecht ist zu pruefen.
