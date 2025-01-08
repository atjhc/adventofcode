patterns = []
with open("input.txt") as file:
	grammar = file.readline().strip().split(", ")
	file.readline()
	for line in file:
		patterns.append(line.strip())

cache = {}
def matches(pattern, grammar):
	if len(pattern) == 0:
		return 1
	if pattern in cache:
		return cache[pattern]
	count = 0
	for rule in grammar:
		if pattern.startswith(rule):
			count += matches(pattern[len(rule):], grammar)
	cache[pattern] = count
	return(count)

count = 0
for pattern in patterns:
	num_matches = matches(pattern, grammar)
	count += num_matches
print(count)