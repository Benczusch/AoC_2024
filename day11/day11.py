import os
test = False
file = "test.txt" if test else "input.txt"

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        else:
            stoneStr = str(stone)
            if len(stoneStr) % 2 == 0:
                mid = len(stoneStr) // 2
                left = stoneStr[:mid]
                right = stoneStr[mid:]
                new_stones.append(int(left))
                new_stones.append(int(right))
            else:
                new_stones.append(stone * 2024)
    return new_stones

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

stones = []
with open(file_path) as f:
    for line in f:
        parts = line.strip().split(" ")
        stones = [int(x) for x in parts]

stoneDict = {}
for stone in stones:
    stoneDict[stone] = stoneDict.get(stone, 0) + 1

for blinkNo in range(25):
    stones = blink(stones)

result1 = len(stones)

#######################################################

for blinkNo in range(75):
    newStoneDict = {}
    for key in stoneDict:
        if key == 0:
            newStoneDict[1] = newStoneDict.get(1, 0) + stoneDict[key]
        else:
            stoneStr = str(key)
            if len(stoneStr) % 2 == 0:
                mid = len(stoneStr) // 2
                left = int(stoneStr[:mid])
                right = int(stoneStr[mid:])
                newStoneDict[left] = newStoneDict.get(left, 0) + stoneDict[key]
                newStoneDict[right] = newStoneDict.get(right, 0) + stoneDict[key]
            else:
                newKey = key * 2024
                newStoneDict[newKey] = newStoneDict.get(newKey, 0) + stoneDict[key]
    stoneDict = newStoneDict
    print(f"After blink {blinkNo+1}")
result2 = sum(newStoneDict.values())

print()
print(f"--- Result of Day {int(11):02d} {('TEST' if test else 'INPUT')} ---")
print(result1)
print(result2)