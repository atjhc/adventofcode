leftList = []
rightMapping = {}

with open("input.txt", "r") as file:
    for line in file:
        left, right = map(int, line.split())
        leftList.append(left)
        if right in rightMapping:
            rightMapping[right] += 1
        else:
            rightMapping[right] = 1

total = 0
for index, leftItem in enumerate(leftList):
    if leftItem in rightMapping:
        count = rightMapping[leftItem]
        print("found: ", leftItem, count, " times")
        total = total + leftItem * count
print(total)