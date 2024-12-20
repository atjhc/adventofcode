import sys
import heapq

class Robot:
	def __init__(self, position, velocity):
		self.position = position
		self.velocity = velocity

	def __repr__(self):
		return f"({self.position}, {self.velocity})"

robots = []
with open("input.txt") as file:
	for line in file:
		parts = line.strip().split(" ")
		position = parts[0].split("=")[1].split(",")
		velocity = parts[1].split("=")[1].split(",")
		robots.append(Robot((int(position[0]), int(position[1])), (int(velocity[0]), int(velocity[1]))))

seconds = 0
width = 101
height = 103

def simulate(seconds):
	quadrants = [0, 0, 0, 0]
	grid = [['.' for _ in range(width)] for _ in range(height)]
	for robot in robots:
		x = (robot.position[0] + robot.velocity[0] * seconds) % width
		y = (robot.position[1] + robot.velocity[1] * seconds) % height
		if grid[y][x] == '.':
			grid[y][x] = 1
		else:
			grid[y][x] += 1
		if x < width // 2:
			if y < height // 2:
				quadrants[0] += 1
			elif y > height // 2:
				quadrants[1] += 1
		elif x > width // 2:
			if y < height // 2:
				quadrants[2] += 1
			elif y > height // 2:
				quadrants[3] += 1
	return (grid, quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

def dfs(grid, x, y):
	if x < 0 or x >= width:
		return 0
	if y < 0 or y >= height:
		return 0
	if grid[y][x] == '.':
		return 0
	grid[y][x] = '.'

	total = 1
	east = dfs(grid, x + 1, y)
	south = dfs(grid, x, y + 1)
	west = dfs(grid, x - 1, y)
	north = dfs(grid, x, y - 1)
	total += east + south + west + north
	return total

def fitness(grid):
	copied = [row[:] for row in grid]
	largest = 0
	for y in range(height):
		for x in range(width):
			score = dfs(copied, x, y)
			if score > largest:
				largest = score
	return largest


def printGrid(grid):
	for row in grid:
		print(''.join(map(str, row)))

# 8736: 68719476736
# 1007424: 68719476736

def equalGrids(lhs, rhs):
	for y in range(height):
		for x in range(width):
			if lhs[y][x] != rhs[y][x]:
				return False
	return True

grid1, score1 = simulate(0)
if len(sys.argv) > 1:
	seconds = int(sys.argv[1])
	printGrid(simulate(seconds)[0])
else:
	heap = []
	for i in range(10403):
		grid, _ = simulate(i)
		fit = fitness(grid)
		heapq.heappush(heap, (fit, i))
		if len(heap) > 20:
			heapq.heappop(heap)
	while heap:
		fit, i = heapq.heappop(heap)
		print(f"{i}: {fit}")
		printGrid(simulate(i)[0])

# grid = [['.' for _ in range(width)] for _ in range(height)]
# for i in range(height):
# 	if i >= width:
# 		continue
# 	grid[i][width // 2 - i // 2] = grid[i][width // 2 + i // 2] = 1
# printGrid(grid)
# print(fitness(grid))
