import os
test = False
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

directions = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
matrix = []
solutions = []
seeds = []
width = 0
height = 0
with open(file_path) as f:
    for line in f:
        width = len(line)
        matrix.append(line.strip())
height = len(matrix)

for row in range(height):
    for col in range(width):
        if matrix[row][col] == 'X':
            seeds.append((row, col))

for seed in seeds:
    for direction in range(8):
        fourth = (seed[0] + 3 * directions[direction][0], seed[1] + 3 * directions[direction][1])
        if 0 <= fourth[0] < height and 0 <= fourth[1] < width:
            second = (seed[0] + directions[direction][0], seed[1] + directions[direction][1])
            third = (seed[0] + 2 * directions[direction][0], seed[1] + 2 * directions[direction][1])
            if matrix[second[0]][second[1]] == 'M' \
                and matrix[third[0]][third[1]] == 'A' \
                and matrix[fourth[0]][fourth[1]] == 'S':
                result1 += 1

for row in range(1, height - 1):
    for col in range(1, width - 1):
        if matrix[row][col] == 'A':
            if (matrix[row - 1][col - 1] == 'M' and matrix[row + 1][col + 1] == 'S' \
                or matrix[row - 1][col - 1] == 'S' and matrix[row + 1][col + 1] == 'M') \
                and \
                (matrix[row - 1][col + 1] == 'M' and matrix[row + 1][col - 1] == 'S' \
                or matrix[row - 1][col + 1] == 'S' and matrix[row + 1][col - 1] == 'M'):
                result2 += 1
                


print(result1)
print(result2)