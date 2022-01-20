#!/usr/bin/env python3

def get_counts_dict(words):
    map = {}
    for word in words:
        lenWord = len(word)
        if lenWord not in map:
            map[lenWord] = 1
        else:
            map[lenWord] += 1
    return map

line = 'this sent ence cont ains only four lett errr words'
print(get_counts_dict(line.strip().split()))