from functools import reduce
from operator import mul

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

seconds = 100
width = 101
height = 103

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
for row in grid:
	print(''.join(map(str, row)))
print(reduce(mul, quadrants))