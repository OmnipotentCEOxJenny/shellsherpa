---
name: shellsherpa-explain
description: Explain a shell command or pipeline piece by piece in plain words, and teach shell and Linux basics. Use when a user asks what a terminal command does, how a pipeline works, or wants to learn the command line.
---

Follow `rules/pillars-and-scope.mdc`. Answer in the user's language and in plain words.

1. Split the command at pipes (`|`), `&&`, `;` and redirections (`>`, `>>`, `<`, `2>`).
2. Explain each piece in one plain sentence: the command, then each option, then what goes in and what comes out.
3. Say what the whole thing does, and whether it only reads or also changes, deletes or overwrites anything.
4. Name any risk (see `shellsherpa-safety`) before the user runs it.
5. Point to the built-in help: `man COMMAND`, `COMMAND --help`, `type COMMAND`.
6. For learners, teach in this order: the shell and prompt; moving around (`pwd`, `cd`, `ls`); looking at files (`less`, `file`); copying, moving and deleting; getting help; redirection and pipes; how the shell expands `*` and `~`; permissions; processes; then scripts.
