#
#   qsort code and a partition function.
#
#   Modify the code so that it returns the number of compares and the number of moves.
#
def partition(lst, lo, hi):
    global numOfCompares
    global numOfSwaps
    part = lo
    while lo < hi:
        numOfCompares += 2
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
            numOfCompares += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1
            numOfCompares += 1
        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]
            numOfSwaps += 3

    numOfCompares += 1
    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        numOfSwaps += 3
    return hi

def rec_qsort(lst, lo, hi):
    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)

def qsort(lst):
    global numOfCompares
    global numOfSwaps
    numOfCompares = 0
    numOfSwaps = 0
    rec_qsort(lst, 0, len(lst) - 1)
    return (numOfCompares, numOfSwaps)