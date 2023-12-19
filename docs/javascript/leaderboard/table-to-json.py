import sys, os
from math import ceil, floor, sqrt, log2
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().strip()
intlist = lambda: [int(i) for i in input().split()]
flolist = lambda: [float(f) for f in input().split()]
mat = lambda a, b, v: [[v] * b for _ in range(a)]
from rich import print
import json
import re

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def debold(ls):
    for i in range(len(ls)):
        ls[i] = ls[i].replace("**", "")
    return ls

def process_sources(s):
    # [source](link) to {Source: source, Link: link}
    s = s.split("](")
    source = s[0][1:]
    link = s[1][:-1]
    return {"Source": source, "Link": link}

# read leaderboard.md table and create a list of dictionaries
with open("leaderboard.md", "r") as f:
    header = f.readline().strip().split("|")
    header = [h.strip() for h in header]
    header = header[1:-1]
    debold(header)
    header = [remove_html_tags(h) for h in header]
    lines = f.readlines()
    lines = [l.strip().split("|") for l in lines]
    lines = [[e.strip() for e in l] for l in lines]
    lines = [[remove_html_tags(e) for e in l] for l in lines]
    lines = [l[1:-1] for l in lines]
    lines = [debold(l) for l in lines]
    lines = lines[1:]
    lines = [dict(zip(header, l)) for l in lines]

for ln in lines:
    ln["Source"] = process_sources(ln["Source"])

with open("leaderboard-data.js", "w") as f:
    f.write("leaderboard = ")
    json.dump(lines, f, indent=4)


