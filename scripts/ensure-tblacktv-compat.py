#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

playlist = Path("playlist.m3u")
text = playlist.read_text(encoding="utf-8")
lines = text.splitlines()
changed = 0
output = []

for line in lines:
    stripped = line.strip()
    if stripped.startswith(("http://", "https://")):
        parts = urlsplit(stripped)
        if parts.path.lower().endswith(".txt") and not parts.fragment:
            stripped = urlunsplit(parts._replace(fragment="/file.txt"))
            prefix = line[: len(line) - len(line.lstrip())]
            line = prefix + stripped
            changed += 1
    output.append(line)

result = "\n".join(output)
if text.endswith("\n"):
    result += "\n"

if result != text:
    playlist.write_text(result, encoding="utf-8")

print(f"TblackTV compatibility: {changed} URL(s) normalized.")
