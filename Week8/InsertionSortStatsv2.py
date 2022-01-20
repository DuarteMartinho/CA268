def insertion_sort(lst):
    # No swap version
    numOfSwaps = 0
    numOfComp = 0
    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        i = todo
        numOfComp += 1
        numOfSwaps += 1
        while i > 0 and tobeinserted < lst[i-1]:
            lst[i] = lst[i-1] # Make space for the item
            numOfSwaps += 1
            i -= 1
            if i != 0:
                numOfComp += 1
        lst[i] = tobeinserted  # Found the place for this item, plonk it in
        numOfSwaps += 1
    return (numOfComp, numOfSwaps)