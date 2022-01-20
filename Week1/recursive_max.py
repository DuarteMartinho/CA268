#!/usr/bin/env python3

def maximum(lst):
    newList = sorted(lst)
    if len(newList) >= 1:
        return newList[len(newList) - 1]