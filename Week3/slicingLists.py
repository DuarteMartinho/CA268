#!/usr/bin/env python3

def get_sliced_lists(list):
    listNoLast = list[:-1]
    listNoFirstOrLast = list[1:-1]
    listReverse = list[::-1]
    return (listNoLast, listNoFirstOrLast, listReverse)

print(get_sliced_lists([1, 2, 3, 4, 5, 6, 7, 8, 9]))