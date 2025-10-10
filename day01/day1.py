import os

test = True

file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

leftlist = []
rightlist = []

with open(file_path) as f:
    for line in f:
        linesplit = line.split()
        leftlist.append(int(linesplit[0]))
        rightlist.append(int(linesplit[1]))

leftlist.sort()
rightlist.sort()

print(sum([abs(a - b) for a, b in zip(leftlist, rightlist)]))

counts = {}
for element in rightlist:
    if element in counts:
        counts[element] += 1
    else:
        counts[element] = 1

errorSum = 0
for element in leftlist:
    errorSum += element * counts.get(element, 0)

print(errorSum)