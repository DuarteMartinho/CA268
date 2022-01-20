#!/usr/bin/env python3
    
def checkPalindrone(left, right, i=0, isPalindrome=True):
    if isPalindrome:
        if left[i] != right[len(right) - 1 - i]:
            isPalindrome = False
        i += 1
        if len(left) > i: 
            return checkPalindrone(left, right, i, isPalindrome)
        else:
            return isPalindrome
    else:
        return False


def is_palindrome(word):
    if len(word) > 1:
        if len(word) % 2 == 0:
            half = len(word) // 2
            half1 = word[:half]
            half2 = word[half:]
            return checkPalindrone(half1, half2)
        else:
            half = len(word) // 2
            half1 = word[:half]
            half2 = word[half + 1:]
            return checkPalindrone(half1, half2)
    else:
        return True

print(is_palindrome('TesfseT'))