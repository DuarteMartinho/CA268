#!/usr/bin/env python3

import sys
word = sys.argv[1]
lenght = len(word)
if lenght % 2 == 0:
    half = lenght // 2
    print(word[half:] )
else:
    print(word[0] + word[-1])