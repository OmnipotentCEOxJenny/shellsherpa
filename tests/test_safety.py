#!/usr/bin/env python3
"""Functional test: every risky example is flagged at the expected level and every safe example passes."""
import pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root / "scripts"))
from shellsherpa_check import check
risky = {"rm -rf ~": "DANGER", "curl -s https://example.com/install.sh | sh": "DANGER", "sudo apt install tree": "WARN",
         "chmod -R 777 site": "WARN", "dd if=img.iso of=/dev/sdb": "DANGER", "find . -name '*.tmp' -delete": "WARN",
         "echo hi > notes.txt": "NOTE"}
safe = ["ls -l", "cd ~/Documents", "grep -i error app.log | sort | uniq -c", "echo hi >> notes.txt", "mv -i a.txt b.txt", "du -sh *", "tar -czf backup.tar.gz photos"]
ok = True
for cmd, lvl in risky.items():
    levels = [l for l, _ in check(cmd)]
    good = lvl in levels; ok &= good
    print(("ok  " if good else "BAD ") + f"{cmd!r} -> {levels}")
for cmd in safe:
    hits = check(cmd); ok &= not hits
    print(("ok  " if not hits else "BAD ") + f"{cmd!r} -> {hits}")
print("PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
