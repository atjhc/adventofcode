import re

patterns = []
with open("input.txt") as file:
	grammar = file.readline().strip().split(", ")
	file.readline()
	for line in file:
		patterns.append(line.strip())

string = "^(" + "|".join(grammar) + ")+$"
regex = re.compile(string)
count = 0
for pattern in patterns:
	if regex.match(pattern):
		count += 1
print(count)