import os

test = False

result1 = 0
result2 = 0
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

def issafe(levels):
    if levels[0] == levels[1]:
        return False
    increase = levels[1] > levels[0]
    
    for i in range(len(levels) - 1):
        a = levels[i]
        b = levels[i + 1]

        if increase and (b - a < 1 or b - a > 3):
            return False
        if not increase and (a - b < 1 or a - b > 3):
            return False
    return True

with open(file_path) as f:
    for line in f:
        linesplit = line.split()
        levels = [int(x) for x in linesplit]
        if issafe(levels):
            result1 += 1
            result2 += 1
        else:
            for exclusionId in range(len(levels)):
                newlevels = levels[:exclusionId] + levels[exclusionId + 1:]
                if issafe(newlevels):
                    result2 += 1
                    break

print(result1)
print(result2)