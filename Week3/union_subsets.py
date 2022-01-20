#!/usr/bin/env python3

def set_stuff(a, b):
    unionSet = a.union(b)
    subset = a.issubset(b)
    superset = a.issuperset(b)
    return (unionSet, subset, superset)

print(set_stuff({1, 2, 3}, {4, 5, 6}))