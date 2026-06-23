# Werkstatt: verwaltung-fachverfahren-kommune

> Keine rechtliche oder datenschutzrechtliche Einzelfallpruefung, keine
> verbindliche Behoerdenentscheidung. Arbeitshilfe ohne Gewaehr. Im
> Einzelfall ist die zustaendige Fachaufsicht, die bzw. der
> Datenschutzbeauftragte oder die Rechtsabteilung zu konsultieren.

Diese Werkstatt-Seite fuehrt ausfuehrlich durch alle Skills dieses Plugins
und zeigt, wie sie kombiniert werden, um typische Fachverfahren und
Buergerdienste einer Kommunalverwaltung strukturiert zu pruefen.

## Typischer Pruefablauf fuer ein Fachverfahren der Buergerdienste

1. **Sachverhalt und Bundesland klaeren.** Vor jeder Pruefung
   dokumentieren, welches Fachgebiet betroffen ist und welches
   Bundesland bzw. welche Kommune zustaendig ist, da Landesrecht und
   kommunale Satzungen erheblich variieren.
2. **Melderechtliche Grundpruefung.** Skill
   `einwohnermeldeamt-ummeldung-checkliste` nutzen, wenn ein An-, Ab-
   oder Ummeldevorgang nach dem Bundesmeldegesetz im Mittelpunkt steht.
3. **Personenstandsrechtliche Pruefung.** Skill
   `standesamt-eheschliessung-unterlagen-pruefung` nutzen, wenn es um die
   Vorbereitung einer Eheschliessung oder Geburtsbeurkundung geht.
4. **Aufenthaltsrechtliche Vorpruefung.** Skill
   `auslaenderbehoerde-aufenthaltstitel-einordnung` nutzen, um eine erste,
   unverbindliche Einordnung des moeglichen Aufenthaltstitels
   vorzunehmen, bevor der Termin bei der Auslaenderbehoerde erfolgt.
5. **Wahlorganisation.** Skill `wahlamt-briefwahl-ablauf-checkliste`
   nutzen, um die Briefwahl- und Wahlvorstandsorganisation vor einer
   anstehenden Wahl zu pruefen.
6. **Kommunales Finanzwesen.** Skill
   `kommunales-finanzwesen-haushaltsrecht-checkliste` nutzen, wenn
   Haushaltssatzung, Nachtragshaushalt oder doppische Buchfuehrung zu
   pruefen sind.
7. **Digitale Buergerdienste pruefen.** Skill
   `buergerportal-omnikanal-konzept-pruefung` und/oder Skill
   `heimat-app-anforderungen-pruefung` nutzen, um digitale Kanaele und
   Apps der Kommune auf Konsistenz, Datenschutz und Barrierefreiheit zu
   pruefen.
8. **Prozessverbesserung.** Skill
   `serviceorientierte-verwaltungsleistung-redesign` nutzen, um eine
   bestehende Verwaltungsleistung aus Buergerperspektive zu
   ueberarbeiten, sobald die fachlichen und rechtlichen
   Rahmenbedingungen aus den vorherigen Schritten geklaert sind.
9. **Schulverwaltung als Spezialfall.** Skill
   `digitales-bildungswesen-schulverwaltung-pruefung` nutzen, wenn ein
   Schultraeger bzw. eine Kommune den Digitalisierungsstand von
   Schulverwaltungsprozessen (z. B. Schulanmeldung,
   Lernplattform-Anbindung, Schulverwaltungssoftware) pruefen moechte.
   Da Schulrecht Landesrecht ist, ist dieser Skill staerker als die
   uebrigen Skills dieses Plugins auf die Klaerung des betroffenen
   Bundeslandes angewiesen, bevor die uebrigen Pruefschritte (Datenschutz,
   IT-Sicherheit, Barrierefreiheit) sinnvoll angewendet werden koennen.

## Typische Stolperfallen

- Landesrecht wird uebersehen: Gemeindeordnung/Kommunalverfassung,
  Landeswahlgesetz und Gemeindehaushaltsverordnung unterscheiden sich
  zwischen den Bundeslaendern erheblich — vor jeder Pruefung das
  betroffene Bundesland klaeren und im Ergebnis explizit benennen.
- Verwechslung von "multikanal" und "omnikanal" bei digitalen
  Buergerdiensten: ohne gemeinsamen Vorgangsstatus ueber alle Kanaele
  bleiben Medienbrueche bestehen, auch wenn mehrere Kanaele angeboten
  werden.
- Aufenthaltsrechtliche Einordnungen werden als verbindlich
  missverstanden: der Skill `auslaenderbehoerde-aufenthaltstitel-einordnung`
  liefert ausdruecklich nur eine vorlaeufige Orientierung ohne
  Bindungswirkung.
- Datenschutzrechtliche Pruefungen bei Apps und Portalen (z. B.
  Auftragsverarbeitung, Drittlandbezug des Hostings) werden erst nach
  der Beschaffungsentscheidung statt vorher vorgenommen.
- Fristen (Melde-, Antrags-, Ruecksendefristen) werden ungeprueft aus
  Modellwissen uebernommen, statt sie im aktuell gueltigen Gesetzes- oder
  Verordnungstext zu verifizieren.

## Hinweis zur Aktualitaet

Vor jeder Pruefung sollten die aktuell gueltigen Fassungen der
einschlaegigen Bundes- und Landesgesetze, Verordnungen und kommunalen
Satzungen herangezogen werden. Der konkrete Wortlaut, Fristen und
Aktenzeichen sind vom Nutzer beizubringen oder als pruefungsbeduerftig zu
kennzeichnen, siehe `../references/zitierweise-verwaltung.md`.
