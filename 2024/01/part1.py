list1 = []
list2 = []

with open("input.txt", "r") as file:
    for line in file:
        left, right = map(int, line.split())
        list1.append(left)
        list2.append(right)

list1.sort()
list2.sort()

total = 0
for index, leftItem in enumerate(list1):
	rightItem = list2[index]
	difference = abs(leftItem - rightItem)
	total = total + difference

print(total)
