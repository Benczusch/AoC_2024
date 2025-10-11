import os
test = False
file = "test.txt" if test else "input.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file)

result1 = 0
result2 = 0

rules = []
updates = []

with open(file_path) as f:
    reading_updates = False
    for line in f:
        if not reading_updates:
            if line.strip() == "":
                reading_updates = True
                continue
            rules.append([int(p) for p in line.strip().split('|')])
        else:
            updates.append([int(p) for p in line.strip().split(',')])

ruleIndex = {}
for idx, rule in enumerate(rules):
    if ruleIndex.get(rule[0]) is None:
        ruleIndex[rule[0]] = [idx]
    else:
        ruleIndex[rule[0]].append(idx)
    if ruleIndex.get(rule[1]) is None:
        ruleIndex[rule[1]] = [idx]
    else:
        ruleIndex[rule[1]].append(idx)
safeUpdates = []
unsafeUpdates = []
for update in updates:
    safe = True
    ruleDone = [False for _ in range(len(rules))]
    activeNumbers = set(update)
    for page in update:
        if not safe:
            break
        if ruleIndex.get(page) is not None:
            for ruleId in ruleIndex[page]:
                if not ruleDone[ruleId]:
                    if rules[ruleId][0] == page:
                        ruleDone[ruleId] = True
                    elif rules[ruleId][1] == page and rules[ruleId][0] in activeNumbers:
                        safe = False
                        break
    if safe:
        safeUpdates.append(update)
    else:
        unsafeUpdates.append(update)

result1 = sum([(update[int((len(update) - 1) / 2)]) for update in safeUpdates])
print(result1)

for update in unsafeUpdates:
    pageIndex = {}
    change = True
    while change:
        change = False
        for idx, page in enumerate(update):
            pageIndex[page] = idx
        for rule in rules:
            if rule[0] in pageIndex and rule[1] in pageIndex:
                idx1 = pageIndex[rule[0]]
                idx2 = pageIndex[rule[1]]
                if idx1 > idx2:
                    update[idx1], update[idx2] = update[idx2], update[idx1]
                    change = True
                    break
    result2 += update[int((len(update) - 1) / 2)]
print(result2)