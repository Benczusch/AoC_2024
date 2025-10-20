import os

test = False
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

drive = []

files = []
empties = []

filePositions = []
emptyPositions = []

position = 0

with open(file_path) as f:
    line = f.readline().strip()
    file = True
    id = 0
    for char in line:
        if file:
            drive += [id for _ in range(int(char))]
            filePositions.append(position)
            position += int(char)
            files.append(int(char))
            id += 1
        else:
            drive += [-1 for _ in range(int(char))]
            emptyPositions.append(position)
            position += int(char)
            empties.append(int(char))
        file = not file

secondDrive = drive.copy()

firstEmpty = 0
lastFile = len(drive) - 1
while firstEmpty < lastFile:
    while drive[firstEmpty] != -1 and firstEmpty < lastFile:
        firstEmpty += 1
    while drive[lastFile] == -1 and firstEmpty < lastFile:
        lastFile -= 1
    if firstEmpty < lastFile:
        drive[firstEmpty], drive[lastFile] = drive[lastFile], drive[firstEmpty]
        firstEmpty += 1
        lastFile -= 1

while len(files) > 0:
    fileSize = files.pop()
    pos = filePositions.pop()
    for i in range(len(empties)):
        if emptyPositions[i] >= pos:
            break
        emptySize = empties[i]
        if emptySize >= fileSize:
            empties[i] -= fileSize
            for j in range(pos, pos + fileSize):
                secondDrive[emptyPositions[i] + j - pos] = secondDrive[j]
                secondDrive[j] = -1
            if empties[i] == 0:
                empties.pop(i)
                emptyPositions.pop(i)
            else:
                emptyPositions[i] += fileSize
            break
for i in range(len(drive)):
    if drive[i] > 0:
        result1 += drive[i] * i
    if secondDrive[i] > 0:
        result2 += secondDrive[i] * i
print()
print(f"--- Result of Day {int(9):02d} {('TEST' if test else 'INPUT')} ---")
print(result1)
print(result2)