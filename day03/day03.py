import os
import re

test = False
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

multi_regex = r"mul\([0-9]+,[0-9]+\)"

with open(file_path) as f:
    line = ""
    for fileLine in f:
        line += fileLine.strip()
    parts = line.split()
    commands = re.findall(multi_regex, line)
    for command in commands:
        nums = command[4:-1].split(",")
        result1 += int(nums[0]) * int(nums[1])
    segments = line.split("don't()")
    clean = segments[0]
    for segment in segments[1:]:
        if "do()" in segment:
            clean += ("|" + segment.split("do()", 1)[1])

    commands = re.findall(multi_regex, clean)
    for command in commands:
        nums = command[4:-1].split(",")
        result2 += int(nums[0]) * int(nums[1])

print(result1)
print(result2)