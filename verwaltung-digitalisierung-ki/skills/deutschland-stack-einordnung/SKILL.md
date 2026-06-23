---
name: deutschland-stack-einordnung
description: "Einordnung der fuer ein Digitalisierungsvorhaben relevanten Deutschland-Stack-Komponente. Methodik Pruefung von Basisdiensten gemeinsam genutzten Plattformen und Zustaendigkeiten im Mehrebenensystem. Output ausformulierte Einordnung mit Empfehlung zur Nutzung bestehender Komponenten statt Eigenentwicklung."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Einordnung relevanter Deutschland-Stack-Komponenten fuer ein Vorhaben

## Zweck / Anwendungsfall

Pruefung, welche Komponenten des sogenannten Deutschland-Stacks
(gemeinsam genutzte Basisdienste und Plattformen der oeffentlichen
Verwaltung, z. B. Nutzerkonten, Zustelldienste, Bezahldienste,
Cloud-Infrastruktur) fuer ein konkretes Digitalisierungsvorhaben relevant
sind, statt eine Eigenentwicklung zu planen. Der Skill wird genutzt, wenn
eine Behoerde ein neues digitales Vorhaben konzipiert und pruefen
moechte, auf welchen bestehenden Bausteinen aufgesetzt werden kann.

## Eingaben

- Kurzbeschreibung des Digitalisierungsvorhabens und seines Zwecks.
- Angabe der benoetigten Funktionsbausteine (z. B. Identifizierung,
  Zustellung, Bezahlung, Formularerstellung, Datenaustausch, Hosting/Cloud).
- Angabe der Zustaendigkeitsebene (Bund, Land, Kommune) und etwaiger
  bestehender IT-Strategien/Architekturvorgaben.
- Informationen zu bereits genutzten Basisdiensten in der Behoerde.

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: Vorhaben, benoetigte Funktionsbausteine und
   Zustaendigkeitsebene erfassen.
2. Pruefen, ob fuer die Identifizierung von Nutzenden bestehende
   Nutzerkonto-Loesungen (BundID, Unternehmenskonto, laenderspezifische
   Servicekonten) genutzt werden koennen (siehe Skill
   `digitale-identitaet-nutzerkonto-auswahl`).
3. Pruefen, ob fuer die Antragsuebermittlung FIT-Connect als gemeinsame
   Zustellinfrastruktur genutzt werden kann (siehe Skill
   `fit-connect-anbindung-checkliste`).
4. Pruefen, ob fuer Formularerstellung und Datenmodellierung bestehende
   FIM-Bausteine genutzt werden koennen (siehe Skill
   `fim-baustein-modellierung`).
5. Pruefen, ob fuer Hosting/Betrieb gemeinsam genutzte Cloud- oder
   Rechenzentrumsinfrastrukturen von Bund/Land/kommunalen
   IT-Dienstleistern zur Verfuegung stehen.
6. Pruefen, ob fuer Bezahlvorgaenge ein gemeinsamer Bezahldienst der
   oeffentlichen Verwaltung vorgesehen ist.
7. Eigenentwicklungsbedarf nur fuer die Funktionsbausteine vorsehen, fuer
   die keine geeignete gemeinsame Komponente existiert, und dies begruenden.
8. Ergebnis mit Komponentenuebersicht und Empfehlung ausformulieren.

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
- Hinweis auf verbleibende Unsicherheiten, insbesondere bei sich noch
  entwickelnden Architekturvorgaben.

## Beispiele

Beispiel (FIKTIV): Eine fiktive Kommune plant ein neues digitales Angebot
zur Online-Terminvergabe mit anschliessender Antragstellung und
Gebuehrenzahlung. Die Pruefung ergibt: fuer die Identifizierung kann die
BundID genutzt werden, fuer die Antragsuebermittlung an das Fachverfahren
FIT-Connect, fuer die Datenmodellierung ein bestehender FIM-Baustein,
sofern fuer die betroffene Leistung vorhanden. Fuer die Terminvergabefunktion
selbst existiert keine bundesweit einheitliche gemeinsame Komponente,
sodass hierfuer eine Beschaffung oder Eigenentwicklung als notwendig
eingeordnet wird.

## Normen und Standards

- IT-Planungsrat-Beschluesse zu gemeinsamen Basisdiensten und Komponenten
  des sogenannten Deutschland-Stacks (Beschlussnummer und Versionsstand
  vor Verwendung verifizieren).
- Onlinezugangsgesetz (OZG) als rechtlicher Rahmen fuer die Bereitstellung
  digitaler Verwaltungsleistungen.
- IT-Staatsvertrag/Vereinbarungen zur Zusammenarbeit von Bund und Laendern
  in der IT, soweit einschlaegig (Fundstelle vor Verwendung verifizieren).
- Architekturvorgaben der jeweiligen IT-Strategie von Bund, Land oder
  Kommune (im Einzelfall zu bestimmen).
