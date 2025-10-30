import os
import numpy as np
import PIL.Image as Image
import matplotlib.pyplot as plt
from scipy.ndimage import binary_erosion as erode

test = False
file = "test.txt" if test else "input.txt"

W,H = (101, 103) if not test else (11, 7)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

robots = []

with open(file_path) as f:
    for line in f:
        parts = line.split("v=")
        x = int(parts[0].split(",")[0].split("=")[1].strip())
        y = int(parts[0].split(",")[1].strip())
        vx = int(parts[1].split(",")[0].strip())
        vy = int(parts[1].split(",")[1].strip())

        robots.append((x, y, vx, vy))

N_steps = 100

endMap = np.zeros((H, W), dtype=int)

quadrants = [[0, 0], [0, 0]]

for robot in robots:
    x, y, vx, vy = robot
    x_new = (x + N_steps * vx) % W
    y_new = (y + N_steps * vy) % H

    endMap[y_new][x_new] += 1

    if x_new < (W // 2) and y_new < (H // 2):
        quadrants[0][0] += 1
    elif x_new > (W // 2) and y_new < (H // 2):
        quadrants[0][1] += 1
    elif x_new < (W // 2) and y_new > (H // 2):
        quadrants[1][0] += 1
    elif x_new > (W // 2) and y_new > (H // 2):
        quadrants[1][1] += 1

for step in range(10000):
    endMap = np.zeros((H, W), dtype=int)
    sym = 0
    robotnow = []
    for robot in robots:
        x, y, vx, vy = robot
        x_new = (x + step * vx) % W
        y_new = (y + step * vy) % H

        endMap[y_new, x_new] += 1
        robotnow.append((x_new, y_new))
    endMap = endMap > 0

    maxLens = (0, 0)

    for robot in robotnow:
        x, y = robot
        downLen = 1
        rightLen = 1
        while endMap[(y + downLen) % H, x]:
            downLen += 1
        while endMap[y, (x + rightLen) % W]:
            rightLen += 1
        if downLen > maxLens[0]:
            maxLens = (downLen, maxLens[1])
        if rightLen > maxLens[1]:
            maxLens = (maxLens[0], rightLen)
    
    if maxLens[0] >= 10 and maxLens[1] >= 10:
        im = Image.fromarray(endMap, mode="1")
        plt.imshow(endMap)
        plt.show()
    

print(quadrants)
print(endMap)
result1 = quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1]

print()
print(f"--- Result of Day {int(14):02d} {('TEST' if test else 'INPUT')} ---")
print(result1)
print(result2)