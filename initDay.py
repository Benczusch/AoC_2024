import os

day_number = input("Enter day number: ")
try:
    day_number = int(day_number)
    if not (1 <= day_number <= 25):
        raise ValueError
except ValueError:
    print("Invalid input. Please enter a number between 1 and 25.")
    exit(1)

day_dir = f"day{int(day_number):02d}"
if not os.path.exists(day_dir):
    os.makedirs(day_dir)
template =  """import os
test = True
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

with open(file_path) as f:
    for line in f:
        parts = line.split()

print()
print(f"--- Result of Day {int(day_number):02d} {('TEST' if test else 'INPUT')} ---")
print(result1)
print(result2)"""

with open(os.path.join(day_dir, f"day{int(day_number):02d}.py"), "w") as f:
    f.write(template)
open(os.path.join(day_dir, "input.txt"), "w").close()
open(os.path.join(day_dir, "test.txt"), "w").close()