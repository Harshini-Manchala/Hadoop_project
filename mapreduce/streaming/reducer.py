#!/usr/bin/env python3
import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    status, c = line.strip().split("\t")
    counts[status] += int(c)

for k, v in counts.items():
    print(k, v)

