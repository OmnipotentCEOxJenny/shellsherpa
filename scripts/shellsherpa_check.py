#!/usr/bin/env python3
"""ShellSherpa safety check for shell commands (standard library only).
Usage: python3 scripts/shellsherpa_check.py FILE   (one command per line; '#' lines ignored)
       echo 'rm -rf ~/old' | python3 scripts/shellsherpa_check.py -
Flags commands that can delete, overwrite or expose data, or run code from the internet, and says why.
It is a pattern list, not a full shell parser: it can miss dangers and cannot prove a command is safe.
Exit 0 = nothing flagged, 1 = at least one warning, 2 = usage error."""
import re, sys

RULES = [
 (r"\brm\s+(-[a-zA-Z]*[rf][a-zA-Z]*\s+)+(/|~|\*|/\*|\$HOME)(\s|$)", "DANGER", "recursive or forced delete of a whole folder tree, home or root: cannot be undone"),
 (r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*f|\brm\s+-[a-zA-Z]*f[a-zA-Z]*r", "WARN", "rm -rf deletes without asking and without a trash can; check the path first (try ls on it)"),
 (r"\b(curl|wget)\b[^|]*\|\s*(sudo\s+)?(ba|z|)sh\b", "DANGER", "runs a script straight from the internet without reading it first"),
 (r"\bsudo\b", "WARN", "runs as the superuser (root); mistakes can damage the whole system"),
 (r"\bchmod\s+(-R\s+)?0?777\b", "WARN", "gives everyone read, write and run permission"),
 (r"\bchmod\s+-R\b|\bchown\s+-R\b", "WARN", "changes permissions or owners for a whole folder tree"),
 (r"\bdd\b.*\bof=/dev/", "DANGER", "dd writing to a device can wipe a disk"),
 (r"\bmkfs(\.\w+)?\b", "DANGER", "formats a disk or partition, erasing it"),
 (r":\(\)\s*\{\s*:\|:&\s*\};:", "DANGER", "fork bomb: floods the system with processes"),
 (r"(^|[^>])>\s*/etc/|>\s*/dev/sd", "DANGER", "overwrites a system file or disk"),
 (r"(^|[^>2&])>\s*[^\s>&|]+", "NOTE", "> replaces the file's contents; use >> to add to the end instead"),
 (r"\bmv\b(?!.*\s-i\b)", "NOTE", "mv overwrites a file with the same name without asking; add -i to be asked"),
 (r"\bkill\s+-9\b|\bkillall\b", "NOTE", "force-stops processes without letting them save"),
 (r"\bfind\b.*\s-delete\b|\bfind\b.*-exec\s+rm\b", "WARN", "find deletes every match; run it without -delete first to see the list"),
 (r"\bhistory\s+-c\b|\bshred\b", "NOTE", "removes history or data permanently"),
]

def check(line):
    out = []
    for pat, level, why in RULES:
        if re.search(pat, line):
            out.append((level, why))
    return out

def main(argv):
    if len(argv) < 2: print(__doc__); return 2
    src = sys.stdin if argv[1] == "-" else open(argv[1], encoding="utf-8")
    flagged = 0
    for n, line in enumerate(src, 1):
        line = line.strip()
        if not line or line.startswith("#"): continue
        hits = check(line)
        if hits:
            flagged += 1
            print(f"line {n}: {line}")
            for level, why in hits: print(f"  {level}: {why}")
        else:
            print(f"line {n}: ok   {line}")
    print("nothing flagged (a pattern check cannot prove a command is safe)" if not flagged else f"{flagged} command(s) flagged")
    return 1 if flagged else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
