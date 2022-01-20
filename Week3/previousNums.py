#!/usr/bin/env python3

def main():
    print("Enter numbers (-1 to end): ", end="")
    num = int(input())
    myList = []
    solution = []
    while num != -1:
        if num in myList:
            solution.append(num)
        myList.append(num)
        num = int(input())
    
    for num in solution:
        print(str(num) + " ", end="")
    print()
if __name__ == "__main__":
    main()