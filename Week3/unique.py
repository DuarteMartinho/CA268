#!/usr/bin/env python3

def unique_list(list):
    output = []
    for x in list:
        if x not in output:
            output.append(x)
    return output