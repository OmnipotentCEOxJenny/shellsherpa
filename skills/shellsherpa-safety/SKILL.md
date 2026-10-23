---
name: shellsherpa-safety
description: Check shell commands for risks such as deleting, overwriting, superuser use or running downloaded scripts, and suggest safer versions. Use before running a command the user found online or is unsure about.
---

Follow `rules/scope.mdc`. Answer in the user's language.

1. Before the user runs a command, check it for: recursive or forced delete (`rm -rf`), `sudo`, piping a download into a shell (`curl ... | sh`), `chmod 777` or recursive permission changes, `dd` to a device, `mkfs`, `>` that would overwrite a file, `mv` without `-i`, `find ... -delete`.
2. If Python is available, run `python3 scripts/shellsherpa_check.py FILE` (or pipe the command in with `-`). It is a pattern list, not a proof of safety.
3. For each risk give: what could go wrong, a safer version (for example `rm -ri`, `mv -i`, `>>`, reading a script before running it), and a preview command that shows what would be affected.
4. Never run a flagged DANGER command for the user without their clear go-ahead after the warning.
