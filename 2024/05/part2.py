from functools import cmp_to_key

rules = {}
lines = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            break
        before, after = map(int, line.split("|"))
        if before not in rules:
            rules[before] = set()
        rules[before].add(after)
    for rule in rules:
        print(f"{rule}|{rules[rule]}")
    for line in file:
        lines.append(list(map(int, line.strip().split(","))))

def isSorted(list):
    for i, page in enumerate(list):
        if page not in rules:
            continue
        rule = rules[page]
        followingPages = list[i + 1:]
        for followingPage in followingPages:
            if followingPage not in rule:
                return False
    return True

def compare(lhs, rhs):
    if lhs not in rules:
        return 0
    if rhs in rules[lhs]:
        return -1
    return 1

total = 0
for line in lines:
    if isSorted(line):
        continue
    sortedLine = sorted(line, key=cmp_to_key(compare))
    if not isSorted:
        print("SOMETHING WRONG")
    middle = sortedLine[len(sortedLine) // 2]
    print(f"{line}\n{sortedLine}")
    total += middle
# for line in lines:
#     if not isSorted(line):
#         continue
#     middle = line[len(line) // 2]
#     total += middle
print(total)
