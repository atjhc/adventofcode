from collections import namedtuple
Equation = namedtuple('Equation', ['total', 'terms'])

equations = []
with open("input.txt", "r") as file:
	for line in file:
		parts = line.split(":")
		total = int(parts[0])
		terms = list(map(int, parts[1].strip().split(" ")))
		equations.append(Equation(total, terms))

def possibleValues(list):
	if len(list) == 1:
		return set(list)
	first = list[:-1]
	last = list[-1]
	totals = set()
	candidates = possibleValues(first)
	for candidate in candidates:
		totals.add(candidate + last)
		totals.add(candidate * last)
		totals.add(int(str(candidate) + str(last)))
	return totals

finalSum = 0
for equation in equations:
	candidates = possibleValues(equation.terms)
	if equation.total in candidates:
		finalSum += equation.total

print(finalSum)