import math
from collections import namedtuple
Location = namedtuple('Location', ['x', 'y'])
EMPTY = "."
ANTINODE = "#"

with open("test.txt") as file:
    board = [list(line.strip()) for line in file]
height = len(board)
width = len(board[0])

antennas = {}
for y, row in enumerate(board):
	for x, value in enumerate(row):
		if value != EMPTY:
			if value not in antennas:
				antennas[value] = set()
			antennas[value].add(Location(x, y))

def calculateAntinodes(first, second):
	delta = Location(first.x - second.x, first.y - second.y)
	antinodes = []
	antinode = first
	while withinBounds(antinode):
		antinodes.append(antinode)
		antinode = Location(antinode.x + delta.x, antinode.y + delta.y)
	antinode = first
	while withinBounds(antinode):
		antinodes.append(antinode)
		antinode = Location(antinode.x - delta.x, antinode.y - delta.y)
	return antinodes

def withinBounds(location):
	return location.x >= 0 and location.x < width and location.y >= 0 and location.y < height

antinodes = [[None for _ in range(width)] for _ in range(height)]
for type in antennas:
	locations = list(antennas[type])
	if len(locations) == 1:
		continue
	for i, first in enumerate(locations):
		remaining = locations[i+1:]
		if len(remaining) == 0:
			break
		for second in remaining:
			antinodes = calculateAntinodes(first, second)
			for antinode in antinodes:
				if withinBounds(antinode):
					board[antinode.y][antinode.x] = ANTINODE

count = 0
for row in board:
	print(''.join(row))
	for value in row:
		if value == ANTINODE:
			count += 1
print(count)






	# difference = Location(first.x - second.x, first.y - second.y)
	# midpoint = Location(math.sqrt(difference.x * difference.x), math.sqrt(difference.y * difference.y))
	# midpointToFirst = Location(first.x - midpoint.x, first.y - midpoint.y)
	# midpointToSecond = Location(second.x - midpoint.x, second.y - midpoint.y)
	# firstAntinode = Location(math.floor(first.x + midpointToFirst.x), math.floor(first.y + midpointToFirst.y))
	# secondAntinode = Location(math.floor(second.x + midpointToSecond.x), math.floor(second.y + midpointToSecond.y))
	# return (firstAntinode, secondAntinode)