#!/usr/bin/env python3

def sum_to_k(list, val):
    sumsFound = []
    for i in list:
        for j in list:
            if j != i and i + j == val:
                newSum = f'{i} + {j}'
                if newSum not in sumsFound:
                    print(i, j)
                    sumsFound.append(f'{i} + {j}')
                    sumsFound.append(f'{j} + {i}')

lst = [1, 6, 7, 8, 9, 10, 2, 3, 4, 5]
k = 13
sum_to_k(lst, k)