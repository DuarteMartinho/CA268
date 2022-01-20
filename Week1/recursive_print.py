#!/usr/bin/env python3

def rprint(a, b):
    print(a)
    a += 1
    if a != b:
        rprint(a, b)