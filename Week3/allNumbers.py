#!/usr/bin/env python3

import sys

def get_evenodd_list():
    newList = []
    for line in sys.stdin:
        line = line.strip()
        if line == '-1':
            break
        else:
            newList.append(int(line))
    odds = [i for i in newList if i % 2 != 0]
    evens = [i for i in newList if i % 2 == 0]
    return (odds, evens)

print(get_evenodd_list())