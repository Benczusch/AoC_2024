import os
import numpy as np

test = False
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

plot_map = []

with open(file_path) as f:
    for line in f:
        plot_map.append(list(line.strip()))

H = len(plot_map)
W = len(plot_map[0])

plot_map = np.array(plot_map)

region_map = np.ones((H, W), dtype=int) * -1

regions = []

for i in range(H):
    for j in range(W):
        if region_map[i, j] < 0:
            region_id = len(regions)
            regions.append([])
            region_type = plot_map[i, j]
            stack = [(i, j)]
            checked = np.zeros((H, W), dtype=bool)
            while stack:
                x, y = stack.pop()
                if checked[x, y]:
                    continue
                checked[x, y] = True
                if plot_map[x, y] == region_type:
                    region_map[x, y] = region_id
                    regions[region_id] = (x, y)

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < H and 0 <= ny < W and not checked[nx, ny]:
                            stack.append((nx, ny))

areas = [0] * len(regions)
perimeters = [0] * len(regions)
corners = [0] * len(regions)

for i in range(H):
    for j in range(W):
        if plot_map[i, j] == 'S':
            pass
        region_id = region_map[i, j]
        areas[region_id] += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = i + dx, j + dy
            if nx < 0 or nx >= H or ny < 0 or ny >= W or region_map[nx, ny] != region_id:
                perimeters[region_id] += 1
        
        windows = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for window in windows:
            across = (i + window[0], j + window[1])
            side1 = (i + window[0], j)
            side2 = (i, j + window[1])
            main_diagonal = 0 <= across[0] < H and 0 <= across[1] < W and region_map[across[0], across[1]] == region_id

            diagonal = 0
            diagonal += 1 if 0 <= side1[0] < H and 0 <= side1[1] < W and region_map[side1[0], side1[1]] == region_id else 0
            diagonal += 1 if 0 <= side2[0] < H and side2[1] < W and region_map[side2[0], side2[1]] == region_id else 0

            if diagonal == 0:
                corners[region_id] += 3
            elif diagonal == 1:
                corners[region_id] += 1 if main_diagonal else 0
            else:
                corners[region_id] += 1 if not main_diagonal else 0

result1 = sum([areas[i] * perimeters[i] for i in range(len(regions))])
result2 = int(sum([areas[i] * corners[i] / 3 for i in range(len(regions))]))

print()
print(f"--- Result of Day {int(12):02d} {('TEST' if test else 'INPUT')} ---")
print(result1)
print(result2)