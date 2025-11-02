import os
import numpy as np
test = False
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

mapLines = []

with open(file_path) as f:
    for line in f:
        mapLines.append(list(line.strip()))

W = len(mapLines[0])
H = len(mapLines)

# 0 - East
# 1 - North
# 2 - West
# 3 - South

pointMap = np.ones([H, W, 4], dtype=np.int64) * 2147483647
pathMap = np.ones([H, W], dtype=np.bool)

endPoint = None

for row in range(H):
    for col in range(W):
        pathMap[row, col] = mapLines[row][col] != '#'
        if mapLines[row][col] == 'S':
            pointMap[row, col, 0] = 0
        if mapLines[row][col] == 'E':
            endPoint = (row, col)

change = True
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
while change:
    change = False
    for row in range(H):
        for col in range(W):
            if pathMap[row, col]:
                for facing in range(4):
                    smallest = 2147483647
                    for turn in range(-1, 3):
                        cost = abs(turn) * 1000
                        potCost = pointMap[row, col, (facing + turn) % 4] + cost
                        if potCost < smallest:
                            smallest = potCost
                    potCost = pointMap[row - directions[facing][0], col - directions[facing][1], facing] + 1
                    if potCost < smallest:
                        smallest = potCost
                    if smallest < pointMap[row, col, facing]:
                        pointMap[row, col, facing] = smallest
                        change = True

result1 = np.min(pointMap[endPoint[0], endPoint[1], :])

onPath = np.zeros([W, H, 4], dtype=np.bool)
onPath[endPoint[0], endPoint[1], :] = pointMap[endPoint[0], endPoint[1], :] == np.min(pointMap[endPoint[0], endPoint[1], :])

change = True
while change:
    change = False
    for row in range(H):
        for col in range(W):
            if not pathMap[row, col]: continue
            for facing in range(4):
                if not onPath[row, col, facing]: continue
                for turn in range(-1, 3):
                    shouldCost = pointMap[row, col, facing] - abs(turn) * 1000
                    if pointMap[row, col, (facing + turn) % 4] == shouldCost:
                        if not onPath[row, col, (facing + turn) % 4]:
                            onPath[row, col, (facing + turn) % 4] = True
                            change = True
                fromplace = (row - directions[facing][0], col - directions[facing][1])
                if pathMap[fromplace[0], fromplace[1]]:
                    shouldCost = pointMap[row, col, facing] - 1
                    if pointMap[fromplace[0], fromplace[1], facing] == shouldCost:
                        if not onPath[fromplace[0], fromplace[1], facing]:
                            onPath[fromplace[0], fromplace[1], facing] = True
                            change = True
print()
for row in range(H):
    for col in range(W):
        result2 += 1 if np.any(onPath[row, col, :]) else 0
        if not pathMap[row, col]:
            print('#', end = '')
        elif any(onPath[row, col, :]):
            print('O', end='')
        else:
            print('.', end='')
    print()

print()
print(f"--- Result of Day {int(16):02d} {('TEST' if test else 'INPUT')} ---")
print(result1)
print(result2)