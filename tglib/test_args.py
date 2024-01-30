
import re

with open('types.py') as r:
    lines = r.readlines()

for line in lines:

    dese_match_2 = re.search(
        r"obj\s*\[\s*'(.*?)'\s*\]\s*=.*res\.get\(\s*'(.*?)'\s*\)",
        line
    )
    dese_match_3 = re.search(
        r"obj\s*\[\s*'(.*?)'\s*\]\s*=.*res\.get\(\s*'(.*?)'\s*\).*if\s*'(.*?)'\s*in\s*res",
        line
    )
    if dese_match_2:
        group = dese_match_2.group(1, 2)
        if not (group[0] == group[1]):
            print(group, lines.index(line))

    if dese_match_3:
        group = dese_match_3.group(1, 2, 3)
        if not (group[0] == group[1] == group[2]):
            print(group, lines.index(line))
