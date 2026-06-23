# Werkstatt: verwaltung-digitalisierung-ki

> Keine rechtliche oder datenschutzrechtliche Einzelfallpruefung, keine
> verbindliche Behoerdenentscheidung. Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

Diese Werkstatt-Seite fuehrt ausfuehrlich durch alle Skills dieses Plugins
und zeigt, wie sie kombiniert werden, um ein Digitalisierungsvorhaben oder
die Digitalisierung einer einzelnen Verwaltungsleistung vollstaendig zu
pruefen.

## Typischer Pruefablauf fuer eine Verwaltungsleistung

1. **Status quo aufnehmen.** Skill `ozg-umsetzung-pruefung` nutzen, um den
   aktuellen Digitalisierungsstand der Leistung (Medienbrueche,
   Nutzerkontoanbindung, Once-Only-Faehigkeit) zu bewerten.
2. **Fachliche Modellierung pruefen oder neu anlegen.** Skill
   `fim-baustein-modellierung` nutzen, um Leistungsbeschreibung,
   Prozessbaustein und Datenfeldbaustein zu pruefen oder zu entwerfen,
   moeglichst unter Wiederverwendung bestehender Bausteine.
3. **Identifizierung klaeren.** Skill
   `digitale-identitaet-nutzerkonto-auswahl` nutzen, um das passende
   Vertrauensniveau und Nutzerkonto-Verfahren zu bestimmen.
4. **Formerfordernisse pruefen.** Skill
   `elektronische-signatur-siegel-einordnung` anwenden, wenn Bescheide,
   Vertraege oder andere formgebundene Dokumente elektronisch ausgestellt
   werden sollen.
5. **Antragsuebermittlung technisch anbinden.** Skill
   `fit-connect-anbindung-checkliste` nutzen, um die Anbindung des
   Fachverfahrens an die Zustellinfrastruktur zu pruefen.
6. **Once-Only und Registeranbindung pruefen.** Skill
   `registermodernisierung-once-only-pruefung` nutzen, um zu pruefen,
   welche Angaben automatisiert aus Registern bezogen werden koennen.
7. **Interoperabilitaet absichern.** Skill
   `interoperabilitaet-datenaustausch-pruefung` nutzen, wenn Daten mit
   weiteren Behoerden oder Fachverfahren ausgetauscht werden.
8. **KI-Komponenten gesondert pruefen.** Skill
   `ki-einsatz-verwaltungsverfahren-pruefung` anwenden, sobald ein
   KI-System zur Vorpruefung, Klassifizierung oder Entscheidungsunterstuetzung
   eingesetzt werden soll.
9. **Automatisierungspotenzial der Bearbeitungsschritte pruefen.** Skill
   `prozessautomatisierung-verwaltungsleistung-pruefung` nutzen, um zu
   klaeren, welche Bearbeitungsschritte sich regelbasiert automatisieren
   lassen (Workflow-Engine, Schnittstellen zu Fachverfahren) und welche
   eine manuelle Bearbeitung erfordern.
10. **Wallet-Einsatz pruefen, falls Nachweise betroffen sind.** Skill
    `eudi-wallet-einsatzpruefung` anwenden, wenn fuer die Leistung
    Nachweise oder Attribute ueber eine digitale Wallet (z. B.
    EUDI-Wallet) ausgestellt oder entgegengenommen werden sollen.
11. **Datengetriebene Auswertung/Open-Data-Bereitstellung pruefen, falls
    einschlaegig.** Skill `datengetriebene-entscheidung-open-data-pruefung`
    nutzen, wenn aus dem Verfahren gewonnene Daten fuer datengetriebene
    Entscheidungen genutzt oder als Open Data veroeffentlicht werden
    sollen.
12. **Barrierefreiheit sicherstellen.** Skill
    `barrierefreiheit-digitale-angebote-pruefung` vor Veroeffentlichung des
    digitalen Angebots anwenden.
13. **Architektur-Einordnung.** Skill `deutschland-stack-einordnung`
    nutzen, um zu pruefen, welche Vorhabenbestandteile auf bestehenden
    gemeinsamen Komponenten aufgesetzt werden koennen, statt sie neu zu
    entwickeln.
14. **IT-Sicherheit als Abschluss-Check pruefen.** Skill
    `it-sicherheit-grundschutz-checkliste` vor Produktivbetrieb anwenden,
    um die grundlegenden BSI-IT-Grundschutz-Anforderungen an das neue
    Verfahren zu pruefen.
15. **Datenschutz-Folgenabschaetzung als Abschluss-Check pruefen.** Skill
    `datenschutz-folgenabschaetzung-pruefung` vor Produktivbetrieb
    anwenden, um zu klaeren, ob fuer das Verfahren eine
    Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO erforderlich ist.

## Typische Stolperfallen

- Eigenentwicklungen werden geplant, ohne vorher zu pruefen, ob ein
  passender FIM-Baustein oder eine gemeinsame Deutschland-Stack-Komponente
  bereits existiert — dies fuehrt zu unnoetigem Mehraufwand und
  Inkompatibilitaeten.
- Die Wahl des Identifizierungsmittels wird unterschaetzt: ein zu
  niedriges Vertrauensniveau kann die Rechtswirksamkeit eines
  Verwaltungsakts gefaehrden, ein zu hohes Niveau schafft unnoetige
  Huerden fuer Nutzende.
- KI-Komponenten werden als reine IT-Funktion behandelt, ohne die
  Anforderungen der EU-KI-Verordnung (insbesondere bei
  Hochrisiko-Einstufung) gesondert zu pruefen.
- Barrierefreiheit wird erst kurz vor Veroeffentlichung statt von Beginn
  an mitgedacht, was nachtraegliche Anpassungen aufwendig macht.
- Once-Only-Versprechen werden kommuniziert, obwohl die technische
  Schnittstelle zum abgebenden Register noch nicht produktiv ist — dies
  transparent machen, statt einen falschen Umsetzungsstand zu suggerieren.

## Hinweis zur Aktualitaet

OZG-Nachfolgeregelungen, IT-Planungsrat-Beschluesse, die FIM- und
XOEV-Standards, das BSI-IT-Grundschutz-Kompendium, der eIDAS-2.0-Rahmen
fuer digitale Wallets sowie die Anwendbarkeit einzelner Vorschriften der
EU-KI-Verordnung entwickeln sich laufend weiter. Vor jeder Pruefung
sollten der aktuelle Versionsstand der einschlaegigen Standards und
Beschluesse sowie die zustaendige Fachaufsicht herangezogen werden, siehe
`../references/zitierweise-verwaltung.md`.
