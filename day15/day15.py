import os
import numpy as np

test = False
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

grid = []
moves = []

starting_pos = (0, 0)

with open(file_path) as f:
    lineId = 0
    for line in f:
        lineArray = list(line.strip())
        if len(lineArray) > 0:
            loc = line.find('@')
            if loc != -1:
                starting_pos = (lineId, loc)
                lineArray[loc] = '.'
            grid.append(lineArray)
        else:
            break
        lineId += 1
    for line in f:
        moves += list(line.strip())

W, H = len(grid[0]), len(grid)

wideGrid = []
for row in grid:
    wideGrid.append([])
    for char in list(row):
        if char == '.':
            wideGrid[-1].append('.')
            wideGrid[-1].append('.')
        elif char == '#':
            wideGrid[-1].append('#')
            wideGrid[-1].append('#')
        elif char == 'O':
            wideGrid[-1].append('[')
            wideGrid[-1].append(']')

def print_grid(grid, position):
    gridCopy = [row.copy() for row in grid]
    for rowid, row in enumerate(gridCopy):
        if position[0] == rowid:
            row[position[1]] = '@'
        print("".join(str(x) for x in row))

pos = starting_pos
for step in moves:
    if step == '^':
        direction = (-1, 0)
    elif step == 'v':
        direction = ( 1, 0)
    elif step == '<':
        direction = (0, -1)
    elif step == '>':
        direction = (0,  1)
    else:
        raise ValueError("Invalid move : " + step)
    endOfLine = (pos[0] + direction[0], pos[1] + direction[1])

    moved = 1

    while True:
        if grid[endOfLine[0]][endOfLine[1]] == '#':
            break
        if grid[endOfLine[0]][endOfLine[1]] == 'O':
            moved += 1
            endOfLine = (endOfLine[0] + direction[0], endOfLine[1] + direction[1])
        elif grid[endOfLine[0]][endOfLine[1]] == '.':
            for _ in range(moved):
                prev = (endOfLine[0] - direction[0], endOfLine[1] - direction[1])
                grid[endOfLine[0]][endOfLine[1]] = grid[prev[0]][prev[1]]
                endOfLine = prev
            grid[pos[0]][pos[1]] = '.'
            pos = (pos[0] + direction[0], pos[1] + direction[1])
            break

for row in range(H):
    for col in range(W):
        if grid[row][col] == 'O':
            result1 += row * 100 + col

pos = (starting_pos[0], starting_pos[1] * 2)

for stepId, step in enumerate(moves):
    if step == '^':
        direction = (-1, 0)
    elif step == 'v':
        direction = ( 1, 0)
    elif step == '<':
        direction = (0, -1)
    elif step == '>':
        direction = (0,  1)
    else:
        raise ValueError("Invalid move : " + step)
    if direction[0] == 0:
        moved = 1
        endOfLine = pos[1] + direction[1]
        while True:
            if wideGrid[pos[0]][endOfLine] in ['[', ']']:
                moved += 1
                endOfLine += direction[1]
            if wideGrid[pos[0]][endOfLine] == '#':
                break
            if wideGrid[pos[0]][endOfLine] == '.':
                for _ in range(moved):
                    wideGrid[pos[0]][endOfLine] = wideGrid[pos[0]][endOfLine - direction[1]]
                    endOfLine -= direction[1]
                pos = (pos[0], pos[1] + direction[1])
                break
    else:
        boxesToMove = []
        spacesToCheck = [(pos[0] + direction[0], pos[1])]
        movable = True
        while spacesToCheck:
            space = spacesToCheck.pop(0)
            content = wideGrid[space[0]][space[1]]
            if content == '.':
                pass
            elif content == '#':
                movable = False
                break
            else:
                if content == '[':
                    spacesToCheck.append((space[0] + direction[0], space[1]))
                    spacesToCheck.append((space[0] + direction[0], space[1] + 1))
                    boxesToMove.append((space[0], space[1]))
                    boxesToMove.append((space[0], space[1] + 1))
                elif content == ']':
                    spacesToCheck.append((space[0] + direction[0], space[1]))
                    spacesToCheck.append((space[0] + direction[0], space[1] - 1))
                    boxesToMove.append((space[0], space[1]))
                    boxesToMove.append((space[0], space[1] - 1))
        if movable:
            while boxesToMove:
                box = boxesToMove.pop(-1)
                boxesToMove = [b for b in boxesToMove if b[0] != box[0] or b[1] != box[1]]
                wideGrid[box[0] + direction[0]][box[1]] = wideGrid[box[0]][box[1]]
                wideGrid[box[0]][box[1]] = '.'
            pos = [pos[0] + direction[0], pos[1]]
pass

for row in range(H):
    for col in range(2 * W):
        if wideGrid[row][col] == '[':
            result2 += row * 100 + col

print()
print(f"--- Result of Day {int(15):02d} {('TEST' if test else 'INPUT')} ---")
print(result1)
print(result2)