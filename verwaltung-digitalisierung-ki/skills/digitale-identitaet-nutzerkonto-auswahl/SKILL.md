---
name: digitale-identitaet-nutzerkonto-auswahl
description: "Auswahl des passenden Identifizierungsmittels fuer eine Verwaltungsleistung. Methodik Pruefung von Vertrauensniveau Zielgruppe und Verfuegbarkeit von BundID Unternehmenskonto und eID-Karte. Output ausformulierte Empfehlung mit Begruendung und Hinweis auf Alternativen."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Auswahl des passenden Identifizierungsmittels fuer eine Verwaltungsleistung

## Zweck / Anwendungsfall

Pruefung, welches Identifizierungsmittel (z. B. BundID mit
Benutzername/Passwort, BundID mit eID-Karte/Online-Ausweisfunktion,
Unternehmenskonto, laenderspezifisches Servicekonto) fuer eine konkrete
Verwaltungsleistung angemessen ist. Der Skill wird genutzt, wenn eine
Behoerde das erforderliche Vertrauensniveau einer Leistung bestimmen und
ein passendes Nutzerkonto-Verfahren auswaehlen moechte.

## Eingaben

- Bezeichnung der Verwaltungsleistung und Rechtsfolge der Identifizierung
  (z. B. Antrag mit Rechtsanspruch, Auskunft, Mitteilung ohne Rechtsfolge).
- Zielgruppe (Privatperson, Unternehmen/Organisation, Behoerde).
- Angabe, ob besonders schutzbeduerftige Daten verarbeitet werden
  (z. B. Sozialleistungen, Gesundheitsdaten).
- Angabe, ob die Leistung eine Schriftform oder qualifizierte
  elektronische Signatur erfordert.
- Informationen zur technischen Anbindungsfaehigkeit der eingesetzten
  Plattform (Unterstuetzung von BundID-Schnittstellen).

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: Leistung, Zielgruppe und Rechtsfolge der
   Identifizierung erfassen.
2. Erforderliches Vertrauensniveau einordnen (niedrig, substanziell, hoch)
   anhand der Sensitivitaet der Leistung und etwaiger gesetzlicher
   Vorgaben.
3. Pruefen, ob ein einfaches Konto (Nutzername/Passwort) ausreicht oder ob
   eine staerkere Identifizierung (eID-Karte/Online-Ausweisfunktion,
   weitere eID-Mittel) erforderlich ist.
4. Bei Unternehmen/Organisationen pruefen, ob das Unternehmenskonto mit
   entsprechender Vertretungsbefugnis-Pruefung passend ist.
5. Pruefen, ob laenderspezifische Servicekonten anstelle oder zusaetzlich
   zur BundID vorgesehen sind und wie die Interoperabilitaet sichergestellt
   wird.
6. Pruefen, ob zusaetzlich eine elektronische Signatur/Siegel erforderlich
   ist (siehe Skill `elektronische-signatur-siegel-einordnung`).
7. Alternativen und Einschraenkungen benennen (z. B. fehlende
   Barrierefreiheit bestimmter Verfahren, Verfuegbarkeit fuer Personen ohne
   Personalausweis mit eID-Funktion).
8. Ergebnis mit begruendeter Empfehlung ausformulieren.

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

Beispiel (FIKTIV): Eine fiktive Behoerde bietet eine Verwaltungsleistung
"Antrag auf Wohngeld" an, bei der personenbezogene, finanziell relevante
Daten verarbeitet werden und ein Rechtsanspruch entstehen kann. Die
Pruefung ergibt ein erforderliches substanzielles bis hohes
Vertrauensniveau, sodass die BundID mit Online-Ausweisfunktion (eID-Karte)
empfohlen wird; ein einfaches Passwort-Konto wird als nicht ausreichend
eingeordnet. Alternativ wird auf bestehende Vor-Ort-Antragsverfahren fuer
Personen ohne eID-Funktion verwiesen.

## Normen und Standards

- Onlinezugangsgesetz (OZG) und Nutzerkonten-Bestimmungen.
- Gesetz ueber Personalausweise und den elektronischen Identitaetsnachweis
  (PAuswG) bzw. Nachfolgeregelungen, Fundstelle vor Verwendung verifizieren.
- eIDAS-Verordnung (EU) Nr. 910/2014 bzw. eIDAS 2.0-Rechtsakte zu
  Vertrauensniveaus, Versionsstand vor Verwendung verifizieren.
- IT-Planungsrat-Beschluesse zu BundID/Nutzerkonten
  (Beschlussnummer vor Verwendung verifizieren).
