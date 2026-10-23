# ShellSherpa

ShellSherpa helps your AI assistant be a patient guide to the terminal, the window where you type commands instead of clicking. Paste in a command you found online and it explains each piece in plain words, says whether it only reads or also changes things, and warns you before anything that could delete files, overwrite them, or run code from the internet. It can also teach the basics step by step. Why would you want this? Typing a command you do not understand is risky, and one wrong letter can erase work. ShellSherpa helps you learn, and it helps you check before you press Enter. It's free.

![ShellSherpa logo](assets/logo.png)

## Project status: done, pending, uncertain
**Done**
- 2026-10-22: v1.0.0 built and pushed to GitHub. Local tests: manifest valid JSON and valid against Cursor's plugin schema, skill and rule front matter valid (`tests/check_frontmatter.py`), and `tests/test_safety.py` confirms the safety check flags 7 risky commands at the expected level and passes 7 safe ones.

**Pending**
- Not tested inside Cursor or Grok yet (no in-app test has been done).
- Not submitted to the marketplace.
- Translated summaries are machine-made and not reviewed by native speakers.

## Quick start
1. Install (see Installation).
2. Ask: "What does `grep -i error app.log | sort | uniq -c` do?"
3. Or: "Is this safe to run? `curl -s https://example.com/install.sh | sh`"

## Installation
Install from this repository: https://github.com/OmnipotentCEOxJenny/shellsherpa (Cursor plugin format: `.cursor-plugin/plugin.json`, `skills/`, `rules/`). Free. No API keys, no accounts, no paid services. The optional safety check needs only Python 3 (standard library).

## Testing
1. `python3 tests/check_frontmatter.py` (needs PyYAML).
2. `python3 tests/test_safety.py`. Expected: PASS.
3. Compare with `examples/README.md`.

## Search keywords
ShellSherpa, JennyEcho, OmnipotentCeo, shell, bash, terminal, CommandLine, linux, unix, OneLiners, scripting, pipes, redirection, grep, sed, awk, permissions, chmod, sudo, filesystem, directories, navigation, wildcards, globbing, aliases, environment, variables, processes, jobs, cron, tar, archives, regex, explain, SafetyCheck, dangerous, LearnLinux, ManPages, sherpa, prompt. The full list with plain-word meanings is in [keywords.md](keywords.md).

## Credits
- Inventor and publisher: Rob Domaine / Omnipotent Media LLC
- Builder: Jenny Echo
- Teaching order and explanations informed by the free book Jenny Echo studied in Course 1: William Shotts, *The Linux Command Line* (linuxcommand.org), licensed CC BY-NC-ND 3.0 US. No text from the book is copied; everything here is written in our own words. ShellSherpa is independent and not endorsed by the author.

## Components
- `skills/shellsherpa-explain`: explain commands and teach the basics.
- `skills/shellsherpa-safety`: check commands for risks and suggest safer versions.
- `scripts/shellsherpa_check.py`: optional pattern-based safety check (standard library only).
- `examples/`: a worked explanation and a safety check run.
- `tests/`: front-matter check and functional safety test.
- `rules/scope.mdc`: the scope.
- `keywords.md`: the search keyword list.

## Languages
The AI answers in the user's language and keeps commands, file names and code unchanged. Summaries in 23 languages are in [TRANSLATIONS.md](TRANSLATIONS.md). They are machine translations, not yet reviewed by native speakers; the English text is authoritative. Each language section in TRANSLATIONS.md also starts with a one-line machine-translation notice in that language.

## License
MIT. See `LICENSE`.

## Honest assessment: what this plugin cannot do
- It has not been tested inside Cursor or Grok yet; only local tests on one computer have been run.
- The safety check is a pattern list, not a full shell parser: it can miss dangers and cannot prove a command is safe.
- Explanations focus on bash on Linux; macOS, other shells and Windows can differ.
- It does not run commands for you unless you ask, and it cannot undo a command after it runs.
- It is not a security audit.
- Marketplace: not submitted; it is not an approved listing.
- Translations are machine-made and not reviewed by native speakers.
- Rules and compliance: it follows all local, county, state and federal laws and every platform's rules, uses no paid services, never bypasses logins or security settings, and never claims a feature it does not have.
