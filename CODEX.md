# Hinweise fuer Codex / ChatGPT-basierte Werkzeuge

Dieses Repository ist primaer fuer Claude Code konzipiert, kann aber auch
mit anderen LLM-Werkzeugen (z. B. Codex/ChatGPT) genutzt werden. Beim
Einsatz solcher Werkzeuge gilt zusaetzlich:

1. **Regelwerk laden:** `CLAUDE.md` und `AGENTS.md` vor der ersten Skill-
   Nutzung vollstaendig einlesen, da viele Tools kein automatisches
   Skill-Routing wie Claude Code besitzen.
2. **Manuelle Skill-Auswahl:** Den passenden Skill-Pfad
   (`<plugin>/skills/<skill-name>/SKILL.md`) explizit referenzieren, da
   ohne Plugin-Mechanismus keine automatische Erkennung erfolgt.
3. **Zitierpflicht gilt unveraendert:** Auch ausserhalb von Claude Code
   duerfen keine Blindzitate erzeugt werden (siehe
   `references/zitierweise-verwaltung.md`).
4. **PR-Workflow:** Bei Pull Requests, die mit Codex erstellt wurden, gilt
   dieselbe Checkliste wie in `CONTRIBUTING.md`. Ein Hinweis im PR-Text,
   dass ein anderes Werkzeug als Claude Code verwendet wurde, ist
   erwuenscht, aber nicht Pflicht.
5. **Keine automatische Mergeberechtigung:** Unabhaengig vom verwendeten
   Werkzeug entscheidet die menschliche Maintainerin/der Maintainer ueber
   das Mergen.

Siehe auch `CODEX_INSTRUCTIONS_SKILL_VEREDELUNG.md` fuer Hinweise zur
Ueberarbeitung ("Veredelung") bestehender Skills.
