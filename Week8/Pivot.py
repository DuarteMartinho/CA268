#
#   Return [] to get your list of numbers.
#
#   Then return a list containing solution(s)
# [12, 24, 16, 22, 8, 19]

def partition(lst, lo, hi):
    if len(lst) == 0:
        return 0
    global solution
    part = lo
    solution.append(lst[lo])
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]

    return hi

def qsort(lst, lo, hi):
    if lo < hi:
        pivot = partition(lst, lo, hi)
        qsort(lst, lo, pivot - 1) # do the left
        qsort(lst, pivot + 1, hi) # do the right



def solution():
    global solution
    solution = []
    lst = [12, 24, 16, 22, 8, 19]
    qsort(lst,  0, len(lst) - 1)
    return solution