#!/usr/bin/env python3

import sys

def get_odd_list():
    newList = []
    for line in sys.stdin:
        line = line.strip()
        if line == '-1':
            break
        else:
            newList.append(int(line))
    return [i for i in newList if i % 2 != 0]

print(get_odd_list())