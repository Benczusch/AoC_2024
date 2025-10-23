import os
import numpy as np

test = False
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

rows = []

with open(file_path) as f:
    for line in f:
        parts = line.split()
        rows.append([ord(c) - ord('0') for c in parts[0]])

heightmap = np.array(rows)

reachable = [[[] for _ in range(heightmap.shape[1])]for _ in range(heightmap.shape[0])]
print(reachable)

distinct = np.zeros_like(heightmap)

for i in range(heightmap.shape[0]):
    for j in range(heightmap.shape[1]):
        if heightmap[i,j] == 9:
            reachable[i][j].append((i,j))
            distinct[i,j] = 1

for height in range(8, -1, -1):
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            if heightmap[i,j] == height:
                if i > 0 and heightmap[i-1,j] == height + 1:
                    reachable[i][j].extend(reachable[i-1][j])
                    distinct[i,j] += distinct[i-1,j]
                if i < heightmap.shape[0]-1 and heightmap[i+1,j] == height + 1:
                    reachable[i][j].extend(reachable[i+1][j])
                    distinct[i,j] += distinct[i+1,j]
                if j > 0 and heightmap[i,j-1] == height + 1:
                    reachable[i][j].extend(reachable[i][j-1])
                    distinct[i,j] += distinct[i,j-1]
                if j < heightmap.shape[1]-1 and heightmap[i,j+1] == height + 1:
                    reachable[i][j].extend(reachable[i][j+1])
                    distinct[i,j] += distinct[i,j+1]

for i in range(heightmap.shape[0]):
    for j in range(heightmap.shape[1]):
        if heightmap[i,j] == 0:
            result1 += len(set(reachable[i][j]))
            result2 += distinct[i,j]

print()
print(f"--- Result of Day {int(10):02d} {('TEST' if test else 'INPUT')} ---")
print(result1)
print(result2)