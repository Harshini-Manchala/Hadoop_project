#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.split()
    if len(parts) > 8:
        print(parts[8] + "\t1")
