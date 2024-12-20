with open("input.txt") as file:
	grid = []
	line = file.readline().strip()
	while line != '':
		grid.append(list(line))
		line = file.readline().strip()
	instructions = []
	for line in file:
		instructions += list(line.strip())
width = len(grid[0])
height = len(grid)

class Location:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return str((self.x, self.y))

def value(grid, location):
	return grid[location.y][location.x]

def setValue(grid, location, value):
	grid[location.y][location.x] = value

def findRobot(grid):
	for y, line in enumerate(grid):
		for x, value in enumerate(line):
			if value == '@':
				return Location(x, y)
	return None

def simulate(grid, instruction):
	robot = findRobot(grid)
	if instruction == '^':
		direction = Location(0, -1)
	elif instruction == '>':
		direction = Location(1, 0)
	elif instruction == 'v':
		direction = Location(0, 1)
	else:
		direction = Location(-1, 0)
	nextRobot = Location(robot.x + direction.x, robot.y + direction.y)
	spaces = 1
	while value(grid, nextRobot) == 'O':
		nextRobot = Location(nextRobot.x + direction.x, nextRobot.y + direction.y)
		spaces += 1
	if value(grid, nextRobot) == '#':
		return
	for _ in range(spaces):
		previous = Location(nextRobot.x - direction.x, nextRobot.y - direction.y)
		setValue(grid, nextRobot, value(grid, previous))
		nextRobot = previous
	setValue(grid, robot, '.')

def score(grid):
	total = 0
	for y, row in enumerate(grid):
		for x, value in enumerate(row):
			if value == 'O':
				total += y * 100 + x
	return total

def show(grid):
	for row in grid:
		print(''.join(row))

for instruction in instructions:
	simulate(grid, instruction)
show(grid)
print(score(grid))