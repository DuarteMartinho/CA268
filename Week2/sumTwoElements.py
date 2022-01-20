#!/usr/bin/env python3

def sum_to_k2(list, val):
    sumsFound = []
    for i in list:
        for j in list:
            if j != i and i + j == val:
                newSum = f'{i} + {j}'
                if newSum not in sumsFound:
                    print(i, j)
                    sumsFound.append(f'{i} + {j}')
                    sumsFound.append(f'{j} + {i}')

def sum_to_k(lst, k):
    lst = sorted(lst)
    i = 0
    j = len(lst) - 1
    while i < len(lst) and j >= 0:
        if i == j:
            i += 1
        elif j < i:
            break
        elif lst[i] + lst[j] < k:
            i += 1
        elif lst[i] + lst[j] == k:
            return True
        elif lst[i] + lst[j] > k:
            j -= 1
    return False
lst = [1, 6, 7, 8, 9, 10, 2, 3, 4, 5, 44]
k = 13
print(' 1', ' True', ' ' + str(sum_to_k([5, 10], 15)))
print(' 2', False, sum_to_k([7], 14))
print(' 3', ' True', ' ' + str(sum_to_k([7, 7], 14)))
print(' 4', False, sum_to_k([3, 7, 13], 14))
print(' 5', False, sum_to_k([5, 10], 13))
print(' 6', ' True', ' ' + str(sum_to_k([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 13)))
print(' 7', False, sum_to_k([2, 4, 6, 8, 10, 12], 13))
print(' 8', ' True', ' ' + str(sum_to_k([2, 4, 6, 8, 10, 12], 14)))
print(' 9', ' True', ' ' + str(sum_to_k([2, 4, 6, 8, 10, 12], 16)))
print('10', ' True', ' ' + str(sum_to_k([1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 40], 41)))