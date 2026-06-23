---
name: fit-connect-anbindung-checkliste
description: "Checkliste zur technischen und organisatorischen Anbindung eines Fachverfahrens an FIT-Connect. Methodik Pruefung von Submission-API Zustellpunkt Schema-Validierung Verschluesselung und Betriebsverantwortung. Output ausformulierte Checkliste mit offenen Punkten und Empfehlung zum naechsten Integrationsschritt."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Checkliste zur FIT-Connect-Anbindung eines Fachverfahrens

## Zweck / Anwendungsfall

Pruefung und Strukturierung der technischen und organisatorischen Schritte,
die notwendig sind, um ein bestehendes Fachverfahren an die
FIT-Connect-Infrastruktur (Zustellplattform fuer Antragsdaten zwischen
Online-Diensten und Behoerden) anzubinden.

## Eingaben

- Bezeichnung des Fachverfahrens und der zustaendigen Behoerde.
- Aktueller Stand der Antragsannahme (E-Mail, Portal-Eigenentwicklung,
  Fachverfahrenshersteller mit/ohne FIT-Connect-Unterstuetzung).
- Angabe, ob ein Zustellpunkt (Destination) bei FIT-Connect bereits
  registriert ist.
- Angabe zum verwendeten Antragsschema (XDOMEA, eigenes Schema, FIM-Datenfeldbaustein).
- Informationen zur Verantwortlichkeit fuer Betrieb und Wartung der
  Anbindung (eigene IT, kommunaler Dienstleister, Landesrechenzentrum).

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: Fachverfahren, technische Umgebung und
   bisherigen Antragsweg erfassen.
2. Pruefen, ob bereits ein FIT-Connect-Zustellpunkt fuer die betroffene
   Verwaltungsleistung existiert oder neu beantragt werden muss.
3. Pruefen, ob die Submission-API (Einreichung von Antragsdaten) durch das
   Fachverfahren oder ein vorgeschaltetes Portal direkt angesprochen werden
   kann oder eine Zwischenkomponente (Konnektor/Middleware) erforderlich ist.
4. Pruefen, ob ein passendes Antrags-/Datenschema vorliegt und gegen die
   FIT-Connect-Schema-Validierung getestet wurde.
5. Verschluesselung und Transportsicherheit pruefen (Ende-zu-Ende-Verschluesselung
   der Antragsdaten, Schluesselverwaltung).
6. Betriebsverantwortung und Monitoring klaeren (wer ueberwacht eingehende
   Zustellungen, wer reagiert auf Fehlzustellungen).
7. Offene Punkte und Abhaengigkeiten (z. B. Beschaffung, Vertragsanpassung
   mit Fachverfahrenshersteller) benennen.
8. Ergebnis mit empfohlenem naechsten Integrationsschritt ausformulieren.

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

Beispiel (FIKTIV): Eine fiktive Kreisverwaltung "Musterkreis" moechte das
Fachverfahren fuer "Elterngeldantraege" an FIT-Connect anbinden. Es besteht
noch kein Zustellpunkt, das Fachverfahren unterstuetzt aber bereits eine
Schnittstelle fuer strukturierte XML-Antraege. Pruefung ergibt: Zustellpunkt
muss neu eingerichtet werden, Antragsschema ist vorhanden und muss gegen
die FIT-Connect-Validierung getestet werden, Betriebsverantwortung liegt
beim Landesrechenzentrum. Empfohlener naechster Schritt: Antrag auf
Einrichtung des Zustellpunkts stellen und Testintegration mit dem
Landesrechenzentrum koordinieren.

## Normen und Standards

- FIT-Connect-Architekturdokumentation und technische Spezifikation
  (Versionsstand vor Verwendung verifizieren).
- Onlinezugangsgesetz (OZG) als rechtlicher Rahmen fuer die
  Antragsuebermittlung.
- IT-Planungsrat-Beschluesse zu FIT-Connect als Basisdienst
  (Beschlussnummer vor Verwendung verifizieren).
- Schema-Standards XDOMEA und FIM-Datenfeldbausteine, soweit einschlaegig.
