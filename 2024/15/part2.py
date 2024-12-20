with open("input.txt") as file:
	grid = []
	line = file.readline().strip()
	while line != '':
		row = []
		for value in list(line):
			if value == '#':
				row += ['#','#']
			elif value == '.':
				row += ['.','.']
			elif value == 'O':
				row += ['[',']']
			elif value == '@':
				row += ['@','.']
		grid.append(row)
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

def push(grid, yDirection, x, y):
	targetValue = value(grid, Location(x, y))
	if targetValue == '#':
		return None
	boxesLeft = []
	boxesRight = []	
	if targetValue == '[':
		thisBox = Location(x, y)
		boxesLeft = push(grid, yDirection, x, y + yDirection)
		boxesRight = push(grid, yDirection, x + 1, y + yDirection)
	elif targetValue == ']':
		thisBox = Location(x - 1, y)
		boxesLeft = push(grid, yDirection, x - 1, y + yDirection)
		boxesRight = push(grid, yDirection, x, y + yDirection)
	elif targetValue == '.':
		return []
	if boxesLeft == None:
		return None
	if boxesRight == None:
		return None
	return [thisBox] + boxesLeft + boxesRight

def simulate(grid, instruction):
	if instruction == '^':
		direction = Location(0, -1)
	elif instruction == '>':
		direction = Location(1, 0)
	elif instruction == 'v':
		direction = Location(0, 1)
	else:
		direction = Location(-1, 0)
	robot = findRobot(grid)
	nextRobot = Location(robot.x + direction.x, robot.y + direction.y)
	if instruction == '^' or instruction == 'v':
		boxes = push(grid, direction.y, nextRobot.x, nextRobot.y)
		if boxes == None:
			return
		for box in boxes:
			setValue(grid, box, '.')
			setValue(grid, Location(box.x + 1, box.y), '.')
		for box in boxes:
			setValue(grid, Location(box.x, box.y + direction.y), '[')
			setValue(grid, Location(box.x + 1, box.y + direction.y), ']')
		setValue(grid, nextRobot, '@')
	else:
		spaces = 1
		while value(grid, nextRobot) == '[' or value(grid, nextRobot) == ']':
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
			if value == '[':
				total += y * 100 + x
	return total

def show(grid):
	for row in grid:
		print(''.join(row))

for instruction in instructions:
	simulate(grid, instruction)
show(grid)
print(score(grid))