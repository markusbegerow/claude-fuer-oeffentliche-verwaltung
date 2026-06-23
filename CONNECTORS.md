# Konnektoren / Datenquellen

Dieses Repository selbst stellt keine Live-Datenintegration bereit. Die
folgende Liste beschreibt, welche externen Datenquellen typischerweise als
**Eingabe** fuer die Skills dieses Repositories dienen und worauf beim
Import zu achten ist.

| Quelle | Typischer Export | Hinweis |
|---|---|---|
| FIM-Baustein-Bibliothek (Föderales Informationsmanagement) | Leistungsbeschreibungen, Datenfelddefinitionen | Stand der Bausteine vor Verwendung pruefen; Bausteine werden laufend ueberarbeitet. |
| FIT-Connect-Portal | Anbindungsdokumentation, Schema-Definitionen | Ersetzt keine eigene Pruefung der technischen Anbindung; Versionsstand pruefen. |
| IT-Planungsrat-Beschlussdatenbank | Beschlusstexte, Standardisierungsdokumente | Keine Blindzitate von Beschlussnummern; Fundstelle vor Verwendung verifizieren. |
| BSI-IT-Grundschutz-Kompendium | Bausteine, Anforderungskataloge | Edition/Stand im Output nennen; Kompendium wird jaehrlich aktualisiert. |
| Behoerdenwegweiser/Servicekonto-Portale (z. B. BundID) | Leistungsbeschreibungen, Verfahrensdokumentation | Keine echten Buerger- oder Kontodaten in dieses Repository einspielen; nur fiktive Beispieldaten verwenden. |

## Hinweis

Die Skills in diesem Repository sind textbasierte Pruefhilfen fuer Claude
Code und vergleichbare Werkzeuge. Eine automatisierte API-Anbindung an die
oben genannten Quellen ist nicht Teil dieses Repositories.
