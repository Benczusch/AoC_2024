import os
import numpy as np
test = False
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

frequencies = []
for i in range(ord('a'), ord('z') + 1):
    frequencies.append(chr(i) )
for i in range(ord('A'), ord('Z') + 1):
    frequencies.append(chr(i) )
for i in range(ord('0'), ord('9') + 1):
    frequencies.append(chr(i))

nodes = {}
for freq in frequencies:
    nodes[freq] = []

map = []

with open(file_path) as f:
    posy = 0
    for line in f:
        line = line.strip()
        map.append(line)
        for posx, char in enumerate(line):
            if char in frequencies:
                nodes[char].append((posx, posy))

        posy += 1

width = len(map[0])
height = len(map)

antinodes = np.zeros((height, width), dtype=bool)
resonant_antinodes = np.zeros((height, width), dtype=bool)

for freq in nodes:
    if len(nodes[freq]) < 2:
        continue
    for i in range(len(nodes[freq]) - 1):
        for j in range(i + 1, len(nodes[freq])):
            x1, y1 = nodes[freq][i]
            x2, y2 = nodes[freq][j]

            antix1 = x1 - (x2 - x1)
            antiy1 = y1 - (y2 - y1)
            antix2 = x2 + (x2 - x1)
            antiy2 = y2 + (y2 - y1)

            if antix1 >= 0 and antix1 < width and antiy1 >= 0 and antiy1 < height:
                antinodes[antix1, antiy1] = True
            if antix2 >= 0 and antix2 < width and antiy2 >= 0 and antiy2 < height:
                antinodes[antix2, antiy2] = True

            dist_gcd = np.gcd(abs(x2 - x1), abs(y2 - y1))
            step_x = (x2 - x1) // dist_gcd
            step_y = (y2 - y1) // dist_gcd
            resonant_antinodes[x1, y1] = True
            x = x1 + step_x
            y = y1 + step_y
            for direction in [1, -1]:
                x = x1 + step_x * direction
                y = y1 + step_y * direction
                while (x >= 0 and x < width and y >= 0 and y < height):
                    resonant_antinodes[x, y] = True
                    x += step_x * direction
                    y += step_y * direction

            

result1 = np.sum(antinodes)
result2 = np.sum(resonant_antinodes)

print()
print(f"--- Result of Day {int(8):02d} {('TEST' if test else 'INPUT')} ---")
print(result1)
print(result2)