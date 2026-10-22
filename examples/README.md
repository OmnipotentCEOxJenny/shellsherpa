# Worked example: explaining a pipeline and checking it first (real run, 2026-10-22)

Question: "What does this do, and is it safe? `grep -i error app.log | sort | uniq -c | sort -rn | head -5`"

**What ShellSherpa explains, piece by piece:**
1. `grep -i error app.log`: show every line of `app.log` that contains "error", ignoring upper and lower case.
2. `| sort`: the pipe `|` sends those lines into `sort`, which puts identical lines next to each other.
3. `| uniq -c`: squeeze identical neighbouring lines into one and count them.
4. `| sort -rn`: sort by that count, biggest first (`-r` reverse, `-n` numbers).
5. `| head -5`: keep only the first five lines.
Result: the five most common error lines with how often each appears. It only reads the file; nothing is changed.

**Safety check** (`examples/commands.txt`, run with `python3 scripts/shellsherpa_check.py examples/commands.txt`):
```
line 2: ok   grep -i error app.log | sort | uniq -c | sort -rn | head -5
line 3: rm -rf ~/Downloads/old
  WARN: rm -rf deletes without asking and without a trash can; check the path first (try ls on it)
line 4: curl -s https://example.com/install.sh | sh
  DANGER: runs a script straight from the internet without reading it first
line 5: chmod -R 777 website
  WARN: gives everyone read, write and run permission
  WARN: changes permissions or owners for a whole folder tree
line 6: ok   echo done >> log.txt
3 command(s) flagged
```
