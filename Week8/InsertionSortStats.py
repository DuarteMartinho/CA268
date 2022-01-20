def insertion_sort(lst):
    # At each pass ensure that that section is sorted.
    numOfSwaps = 0
    numOfComp = 0
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        numOfComp += 1
        i = todo
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            numOfSwaps += 1
            i -= 1
            if i != 0:
                numOfComp += 1
    
    return (numOfComp, numOfSwaps)