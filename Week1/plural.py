#!/usr/bin/env python3

consoants = ['a', 'e', 'i', 'o', 'u']
def get_plural(word):
    if len(word) >= 1 and word[-2:] == 'ch' or word[-2:] == 'sh' or word[-1:] == 'x' or word[-1:] == 's' or word[-1:] == 'z':
        newWord = word + 'es'
    elif len(word) >= 2 and word[-2] not in consoants and word[-1:] == 'y':
        newWord = word[:-1] + 'ies'
    elif len(word) >= 1 and word[-1:] == 'f':
        newWord = word[:-1] + 'ves'
    elif len(word) >= 2 and word[-2:] == 'fe':
        newWord = word[:-2] + 'ves'
    elif len(word) >= 1 and word[-1:] == 'o':
        newWord = word + 'es'
    else:
        newWord = word + 's'
    return newWord