#!/usr/bin/env python3

import sys

def make_map():
    newMap = {}
    for line in sys.stdin:
        line = line.strip().split()
        if len(line) == 2:
            name, mark = line
            newMap[name] = mark
    return newMap