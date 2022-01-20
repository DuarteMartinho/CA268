#!/usr/bin/env python3

def get_counts(list):
    trackCounts = [0] * 10
    for word in list:
        lenWord = len(word)
        trackCounts[lenWord] += 1
    return trackCounts

print(get_counts(["cat", "dog", "pig", "ability", "babysit", "pat", "bun"]))