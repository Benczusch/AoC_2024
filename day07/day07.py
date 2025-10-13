import os
test = False
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

with open(file_path) as f:
    for line in f:
        parting1 = line.strip().split(':')
        parting2 = parting1[1].strip().split(' ')

        desired = int(parting1[0])
        equation = [int(x) for x in parting2]

        possibles = [equation[0]]
        possibles2 = [equation[0]]

        for i in range(1, len(equation)):
            newpossibles = []
            for p in possibles:
                newpossibles.append(p + equation[i])
                newpossibles.append(p * equation[i])
            possibles = newpossibles
        if desired in possibles:
            result1 += desired

        for i in range(1, len(equation)):
            newpossibles = []
            for p in possibles2:
                if p <= desired:
                    newpossibles.append(p + equation[i])
                    newpossibles.append(p * equation[i])
                    newpossibles.append(int(str(p) + str(equation[i])))
            possibles2 = newpossibles
        if desired in possibles2:
            result2 += desired

print("\n")
print(result1)
print(result2)