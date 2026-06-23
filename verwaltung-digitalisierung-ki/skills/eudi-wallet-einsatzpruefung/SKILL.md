---
name: eudi-wallet-einsatzpruefung
description: "Pruefung ob und wie eine digitale Wallet zum Beispiel die EUDI-Wallet zur Vorlage von Nachweisen oder Attributen fuer eine Verwaltungsleistung genutzt werden kann. Methodik Analyse der benoetigten Nachweise Pruefung der Ausstellung als Attestierung Pruefung des Empfangs und der Verifikation durch die Behoerde Einordnung in den eIDAS-Rahmen. Output ausformulierter Pruefbericht mit Eignungseinschaetzung je Nachweis und offenen technischen Voraussetzungen."
---

> Dieser Skill ersetzt keine rechtliche, datenschutzrechtliche oder
> IT-sicherheitsrechtliche Einzelfallpruefung durch die zustaendige
> Fachstelle (z. B. Rechtsamt/Justiziariat, Datenschutzbeauftragte,
> IT-Sicherheitsbeauftragte) und keine verbindliche Entscheidung der
> zustaendigen Behoerde. Die Ausgabe ist eine Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

# Pruefung des Wallet-Einsatzes (EUDI-Wallet) fuer eine Verwaltungsleistung

## Zweck / Anwendungsfall

Pruefung, ob fuer eine konkrete Verwaltungsleistung Nachweise oder
Attribute ueber eine digitale Wallet, insbesondere die European Digital
Identity Wallet (EUDI-Wallet) im Rahmen des eIDAS-Rechtsrahmens, entgegen-
genommen oder ausgestellt werden koennen. Der Skill wird genutzt, wenn
eine Behoerde prueft, ob sie als ausstellende Stelle (z. B. fuer
Bescheinigungen, Berechtigungen, Fuehrerscheine) oder als pruefende Stelle
(Verifizierer von vorgelegten Nachweisen) im Wallet-Oekosystem auftreten
soll oder kann.

## Eingaben

- Bezeichnung der Verwaltungsleistung und der dabei benoetigten oder
  ausgestellten Nachweise (z. B. Meldebescheinigung, Fuehrerschein,
  Studienbescheinigung, Gewerbeerlaubnis).
- Angabe, ob die Behoerde als ausstellende Stelle (Issuer), als pruefende
  Stelle (Verifier) oder beides auftreten soll.
- Aktueller Nachweisweg (Papierdokument, PDF, bereits vorhandene
  digitale Bescheinigung).
- Informationen zum technischen Reifegrad der Behoerde (vorhandene
  PKI-Infrastruktur, Anbindung an nationale eID-Vertrauensdienste).
- Angabe, ob der Nachweis bereits in einem strukturierten Datenmodell
  (z. B. FIM-Datenfeldbaustein) vorliegt.

## Ablauf / Checkliste

1. Sachverhalt aufbereiten: Verwaltungsleistung, betroffener Nachweis und
   gewuenschte Rolle der Behoerde (Issuer/Verifier) erfassen.
2. Pruefen, ob der Nachweis inhaltlich fuer eine Attestierung (Attribute
   Attestation) im Sinne des eIDAS-Rahmens geeignet ist, d. h. ob es sich
   um ein klar abgrenzbares, von der Behoerde bestaetigtes Attribut oder
   Dokument handelt.
3. Pruefen, welche Vertrauensstufe fuer die Ausstellung erforderlich ist
   und ob die Behoerde bereits ueber die notwendige technische und
   organisatorische Infrastruktur (qualifizierte elektronische Siegel/
   Signatur, Anbindung an einen Vertrauensdienst) verfuegt — Bezug zu
   Skill `elektronische-signatur-siegel-einordnung`.
4. Pruefen, ob fuer den Empfang vorgelegter Wallet-Nachweise eine
   Verifikationsschnittstelle (z. B. ueber einen OpenID4VP-basierten
   Pruefdienst) vorgesehen oder bereits vorhanden ist.
5. Datenschutzrechtliche Aspekte pruefen: Datenminimierung bei selektiver
   Offenlegung (selective disclosure), Speicherung und Loeschung
   uebermittelter Attribute bei der Behoerde — Bezug zu Skill
   `datenschutz-folgenabschaetzung-pruefung`.
6. Pruefen, ob eine Once-Only-faehige Anbindung an bestehende Register
   sinnvoll ist, statt Attribute doppelt zu erfassen — Bezug zu Skill
   `registermodernisierung-once-only-pruefung`.
7. Technische und organisatorische Voraussetzungen sowie offene Fragen
   (z. B. nationale Umsetzung, Zertifizierungspflichten, Zeitplan der
   eIDAS-2.0-Einfuehrung) benennen.
8. Ergebnis mit Eignungseinschaetzung je Nachweis ausformulieren.

## Quellenpflicht

Verbindlich: `../../../references/zitierweise-verwaltung.md`. Keine
Blindzitate zu Beschlussnummern, Versionsstaenden oder Paragrafen — diese
sind vom Nutzer zu verifizieren oder als pruefungsbeduerftig zu
kennzeichnen. Der eIDAS-2.0-Rahmen und die zugehoerigen
Durchfuehrungsrechtsakte entwickeln sich laufend weiter; Fundstellen und
Anwendbarkeitsdaten sind vor Verwendung zu verifizieren.

## Ausgabeformat

- Vollstaendig ausformulierte Pruefung im Pruefberichtsstil, kein reines
  Stichpunkt-Endergebnis.
- Stand-Datum angeben.
- Klar abgegrenztes Ergebnis am Ende ("Ergebnis: ...").
- Hinweis auf verbleibende Unsicherheiten, insbesondere zum laufenden
  nationalen Umsetzungsstand der eIDAS-2.0-Vorgaben.

## Beispiele

Beispiel (FIKTIV): Eine fiktive Kreisverwaltung prueft, ob sie
Fuehrerscheine zukuenftig zusaetzlich als digitalen Nachweis in einer
EUDI-Wallet ausstellen kann, damit Buergerinnen und Buerger den Nachweis
bei einer Verkehrskontrolle oder Fahrzeuganmietung digital vorlegen
koennen. Die Pruefung ergibt: Der Fuehrerschein ist inhaltlich fuer eine
Attestierung geeignet (klar abgrenzbares, amtlich bestaetigtes Attribut),
die Kreisverwaltung verfuegt jedoch noch nicht ueber eine Anbindung an
einen qualifizierten Vertrauensdienst fuer die Ausstellung signierter
Attestierungen. Empfehlung: Abstimmung mit der zustaendigen Landesbehoerde
zur geplanten Pilotierung des digitalen Fuehrerscheins, keine
eigenstaendige technische Umsetzung vor Klaerung der zentralen
Infrastruktur und des nationalen Zeitplans.

## Normen und Standards

- Verordnung (EU) Nr. 910/2014 (eIDAS-Verordnung) in der durch die
  eIDAS-2.0-Novelle geaenderten Fassung (Fundstelle und Anwendbarkeitsdatum
  vor Verwendung verifizieren).
- Durchfuehrungsrechtsakte zum European Digital Identity Framework
  (technische Spezifikationen, Architecture and Reference Framework;
  Versionsstand vor Verwendung verifizieren).
- Allgemeine Datenschutz-Grundverordnung (DSGVO) hinsichtlich
  Datenminimierung und Zweckbindung bei der Attributuebermittlung.
- Nationales Umsetzungsgesetz zur eIDAS-2.0-Novelle, soweit vorhanden
  (Fundstelle vor Verwendung verifizieren).
