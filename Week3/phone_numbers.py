#!/usr/bin/env python3

def addPhone(phoneBook, name, number):
    phoneBook[name] = number

def queryPhone(phoneBook, name):

    if name in phoneBook:
        number = phoneBook[name]
        return f'{name} has number {number}'
    else:
        return f'Sorry, there is no {name}'

phoneBook = {}
print("Enter a name and number, or a name and ? to query (!! to exit)")
lineIn = input()
while True:
    line = lineIn.strip().split()
    if len(line) == 1 and line[0] == '!!':
        print(f'Bye')
        break
    elif len(line) == 2 and line[1] == "?":
        name = line[0]
        print(queryPhone(phoneBook, name))
    else:
        name = line[0]
        number = int(line[1])
        addPhone(phoneBook, name, number)
    lineIn = input()
