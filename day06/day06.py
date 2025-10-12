import os
import copy
test = False
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

obstacleMap = []

startingPosition = (0, 0)
startingDirection = 0  # 0 right, 1 up, 2 left, 3 down

pos = (0, 0)
dir = 0  # 0 right, 1 up, 2 left, 3 down

with open(file_path) as f:
    for line in f:
        obstacleMap.append([p == '#' for p in line.strip()])
        if '^' in line:
            startingPosition = (len(obstacleMap) - 1, line.index('^'))
            startingDirection = 1  # up

height = len(obstacleMap)
width = len(obstacleMap[0])

pos = startingPosition
dir = startingDirection

visited = [[False for _ in range(width)] for _ in range(height)]
visited[pos[0]][pos[1]] = True

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # right, up, left, down
out = False
disturbPoints = set()
while not out:
    while True:
        nextplace = (pos[0] + directions[dir][0], pos[1] + directions[dir][1])
        if nextplace[0] < 0 or nextplace[0] >= height or nextplace[1] < 0 or nextplace[1] >= width:
            out = True
            break
        if obstacleMap[nextplace[0]][nextplace[1]]:
            dir = (dir - 1) % 4
        else:
            pos = nextplace
            disturbPoints.add(pos)
            visited[pos[0]][pos[1]] = True
            break

result1 = sum([sum([1 if v else 0 for v in row]) for row in visited])

for newObstacle in disturbPoints:
    if newObstacle == startingPosition:
        continue
    currentObstacleMap = copy.deepcopy(obstacleMap)
    currentObstacleMap[newObstacle[0]][newObstacle[1]] = True

    visited = set()
    visited.add((startingPosition[0], startingPosition[1], startingDirection))

    pos = startingPosition
    dir = startingDirection

    out = False
    revisited = False

    rotations = 0

    while not out and not revisited:
        while True:
            nextplace = (pos[0] + directions[dir][0], pos[1] + directions[dir][1])
            if nextplace[0] < 0 or nextplace[0] >= height or nextplace[1] < 0 or nextplace[1] >= width:
                out = True
                break
            if currentObstacleMap[nextplace[0]][nextplace[1]]:
                dir = (dir - 1) % 4
                rotations += 1
                if rotations > 4:
                    revisited = True
                    result2 += 1
                    break
            else:
                pos = nextplace
                if (pos[0], pos[1], dir) in visited:
                    revisited = True
                    result2 += 1
                visited.add((pos[0], pos[1], dir))
                rotations = 0
                break

print(result1)
print(result2)