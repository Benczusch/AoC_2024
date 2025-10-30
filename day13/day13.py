import os
import numpy as np

test = False
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

matrices = []
vectors = []

with open(file_path) as f:
    lines = f.read().splitlines()
    for lineId in range(len(lines) // 4 + 1):
        line1 = lines[lineId * 4 + 0]
        line1split = line1.split(',')
        line2 = lines[lineId * 4 + 1]
        line2split = line2.split(',')
        line3 = lines[lineId * 4 + 2]
        line3split = line3.split(',')
        
        newMatrix = np.zeros((2,2), dtype=np.int64)
        newVector = np.zeros(2, dtype=np.int64)

        newMatrix[0,0] = int(line1split[0].split('+')[1].strip())
        newMatrix[0,1] = int(line2split[0].split('+')[1].strip())
        newMatrix[1,0] = int(line1split[1].split('+')[1].strip())
        newMatrix[1,1] = int(line2split[1].split('+')[1].strip())

        newVector[0] = int(line3split[0].split('=')[1].strip())
        newVector[1] = int(line3split[1].split('=')[1].strip())

        matrices.append(newMatrix)
        vectors.append(newVector)

for i in range(len(matrices)):
    matrix = matrices[i]
    vector = vectors[i]

    det = matrix[0,0] * matrix[1,1] - matrix[0,1] * matrix[1,0]
    if det == 0:
        continue

    sol1 = matrix[1,1] * vector[0] - matrix[0,1] * vector[1]
    sol2 = -matrix[1,0] * vector[0] + matrix[0,0] * vector[1]

    if sol1 % det == 0 and sol2 % det == 0:
        sol1 //= det
        sol2 //= det

        tokens = sol1 * 3 + sol2
        
        result1 += tokens

    altVector = vector + 10000000000000
    sol1 = matrix[1,1] * altVector[0] - matrix[0,1] * altVector[1]
    sol2 = -matrix[1,0] * altVector[0] + matrix[0,0] * altVector[1]
    if sol1 % det == 0 and sol2 % det == 0:
        sol1 //= det
        sol2 //= det

        tokens = sol1 * 3 + sol2
        
        result2 += tokens

print()
print(f"--- Result of Day {int(13):02d} {('TEST' if test else 'INPUT')} ---")
print(result1)
print(result2)