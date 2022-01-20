#!/usr/bin/env python3

def sumto(a, b, total=0):
    if a < b:
        total += a
        a += 1
        return sumto(a, b, total)
    else:
        return total

print(sumto(101, 101))