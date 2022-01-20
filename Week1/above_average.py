#!/usr/bin/env python3

def above_average(list):
    total = sum(list)
    average = total / len(list)
    newList = [i for i in list if i > average]
    return newList