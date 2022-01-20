#!/usr/bin/env python3

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
students = []
deliquents = []

with open(file1, 'r') as f1:
    for line in f1:
        line = line.strip()
        students.append(line)

with open(file2, 'r') as f2:
    for line in f2:
        line = line.strip()
        deliquents.append(line)

output = []
for student in students:
    if student in deliquents:
        output.append(student)
output = sorted(output, key=lambda x: x)

i = 0
while i < len(output):
    print(f'{i + 1}. {output[i]}')
    i += 1