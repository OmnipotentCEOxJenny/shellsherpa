# Changelog

## 1.0.1 (2026-10-23)
- Translations: each language section in TRANSLATIONS.md now starts with a one-line notice in that language saying it is a machine translation, not reviewed by a native speaker, and that the English version is authoritative. README Languages section notes this. No behavior changes.
- Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.0 (2026-10-22)
- First version: skills `shellsherpa-explain` and `shellsherpa-safety`, rule `pillars-and-scope.mdc`, optional safety check `scripts/shellsherpa_check.py`, worked example, plain-language README.
- Informed by Course 1 (William Shotts, The Linux Command Line); no text copied.
- Tests: `tests/check_frontmatter.py` and `tests/test_safety.py`.
- 40 search keywords (single words lowercase, joined words PascalCase, no hyphens, ShellSherpa-specific, per Rob's keyword rules) in the manifest plus `keywords.md`; 23 machine-translated summaries (not native-reviewed).
- Local tests only; not tested in-app. Not submitted to the marketplace.
