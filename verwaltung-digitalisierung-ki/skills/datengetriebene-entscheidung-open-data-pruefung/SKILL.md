---
name: datengetriebene-entscheidung-open-data-pruefung
description: "Pruefung der Voraussetzungen fuer datengetriebene Entscheidungen einer Behoerde oder die Bereitstellung von Verwaltungsdaten als Open Data. Methodik Pruefung der Rechtsgrundlage Pruefung der Datenqualitaet und Data Governance Pruefung von Anonymisierung und Re-Identifikationsrisiko Einordnung nach den Open-Data- und Open-Government-Vorgaben. Output ausformulierter Pruefbericht mit Eignungseinschaetzung und offenen Voraussetzungen."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Pruefung datengetriebener Entscheidungen und der Open-Data-Bereitstellung

## Zweck / Anwendungsfall

Pruefung der Voraussetzungen dafuer, dass eine Behoerde (a) Entscheidungen
oder Planungen auf Basis vorhandener Verwaltungsdaten datengetrieben
unterstuetzt oder (b) Verwaltungsdaten als Open Data veroeffentlicht. Der
Skill wird genutzt, wenn ein Fachbereich oder eine Statistikstelle
vorhandene Datenbestaende fuer eine systematische Auswertung oder fuer die
Bereitstellung an die Oeffentlichkeit nutzen moechte und vorab klaeren
muss, ob Rechtsgrundlage, Datenqualitaet und Datenschutz dies zulassen.

## Eingaben

- Beschreibung des Datenbestands (Inhalt, Herkunft, Erhebungszweck,
  Aktualisierungsfrequenz).
- Angabe des Verwendungszwecks: interne datengetriebene Entscheidung/
  Planung oder externe Veroeffentlichung als Open Data.
- Angabe, ob der Datenbestand Personenbezug aufweist oder personenbeziehbar
  ist, und falls ja, in welchem Detailgrad (Einzeldatensatz, aggregiert).
- Informationen zur bisherigen Datenqualitaet (Vollstaendigkeit,
  Aktualitaet, Konsistenz, bekannte Fehlerquellen).
- Angabe, ob eine Data-Governance-Struktur (Verantwortlichkeiten,
  Datenkatalog, Qualitaetssicherungsprozess) bereits existiert.

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: Datenbestand, Verwendungszweck und
   Personenbezug strukturiert erfassen.
2. Rechtsgrundlage pruefen: auf welcher Befugnisnorm beruht die Erhebung
   der Daten und deckt diese auch die geplante Weiterverarbeitung
   (datengetriebene Entscheidung) oder Veroeffentlichung (Open Data) ab.
3. Bei Personenbezug pruefen, ob eine Anonymisierung oder Pseudonymisierung
   moeglich und ausreichend ist, und das Re-Identifikationsrisiko bei
   kleinen Fallzahlen oder Kombination mit weiteren oeffentlich verfuegbaren
   Datenquellen einschaetzen.
4. Datenqualitaet pruefen: Vollstaendigkeit, Aktualitaet und Konsistenz
   des Datenbestands fuer den vorgesehenen Zweck bewerten; Eignung fuer
   automatisierte oder algorithmengestuetzte Auswertung gesondert pruefen.
5. Data-Governance pruefen: Zustaendigkeiten fuer Datenpflege, -qualitaet
   und -freigabe benennen; pruefen, ob ein Datenkatalog/Metadatenschema
   vorhanden ist.
6. Bei datengetriebenen Entscheidungen pruefen, ob die Entscheidung
   vollstaendig automatisiert erfolgen soll (Bezug zu Skill
   `ki-einsatz-verwaltungsverfahren-pruefung` und zu Vorschriften zur
   automatisierten Entscheidungsfindung) oder lediglich eine
   Entscheidungsgrundlage liefert.
7. Bei Open-Data-Veroeffentlichung pruefen, welches offene Format, welche
   Lizenz (z. B. Datenlizenz Deutschland) und welcher Veroeffentlichungsweg
   (Open-Data-Portal) in Betracht kommen.
8. Risiken benennen (Fehlinterpretation aggregierter Daten durch Dritte,
   Reputationsrisiko bei Datenqualitaetsmaengeln, Re-Identifikationsrisiko).
9. Ergebnis mit Eignungseinschaetzung und offenen Voraussetzungen
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
- Hinweis auf verbleibende Unsicherheiten, insbesondere zum
  Re-Identifikationsrisiko.

## Beispiele

Beispiel (FIKTIV): Eine fiktive Stadtverwaltung moechte Daten zur
Auslastung staedtischer Parkflaechen als Open Data veroeffentlichen, um
Anbieter von Navigations-Apps zu unterstuetzen. Die Pruefung ergibt: Der
Datenbestand enthaelt keine personenbezogenen Daten (ausschliesslich
aggregierte Belegungszahlen je Parkflaeche und Zeitintervall), eine
Rechtsgrundlage fuer die Veroeffentlichung ist ueber die allgemeine
Aufgabennorm zur Bereitstellung amtlicher Informationen gegeben, die
Datenqualitaet ist fuer die letzten zwoelf Monate vollstaendig. Empfehlung:
Veroeffentlichung im offenen Format unter einer offenen Datenlizenz ueber
das zustaendige Open-Data-Portal, vorherige Pruefung der Aktualisierungs-
frequenz und Festlegung einer verantwortlichen Stelle fuer die
Datenpflege.

## Normen und Standards

- Gesetz zur Festlegung eines Rahmens fuer die Weiterverwendung von
  Informationen oeffentlicher Stellen (Open-Data-Gesetz/PSI-Umsetzung,
  Fundstelle vor Verwendung verifizieren).
- Allgemeine Datenschutz-Grundverordnung (DSGVO), insbesondere zu
  Anonymisierung, Pseudonymisierung und Zweckbindung.
- Onlinezugangsgesetz (OZG) und Registermodernisierungsgesetz hinsichtlich
  Datenweiterverwendung zwischen Behoerden.
- Datenlizenz Deutschland bzw. vergleichbare offene Lizenzmodelle fuer
  Verwaltungsdaten (Versionsstand vor Verwendung verifizieren).
- Landesspezifische Open-Data- bzw. Transparenzgesetze, soweit einschlaegig
  (Fundstelle vor Verwendung verifizieren).
