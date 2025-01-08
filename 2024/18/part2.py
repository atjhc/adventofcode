import math

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

WALL = '#'

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def north(self):
        return Location(self.x, self.y - 1)

    def east(self):
        return Location(self.x + 1, self.y)

    def south(self):
        return Location(self.x, self.y + 1)

    def west(self):
        return Location(self.x - 1, self.y)

    def move(self, direction):
        funcs = [self.north, self.east, self.south, self.west]
        return funcs[direction]()

    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y

    def __repr__(self):
        return f"{self.x},{self.y}"

width = height = 71
events = []
with open("input.txt") as file:
    for line in file:
        x, y = line.strip().split(",")
        events.append(Location(int(x), int(y)))

def getValue(data, location):
    return data[location.y][location.x]

def setValue(data, location, value):
    data[location.y][location.x] = value

def show(grid):
	for row in grid:
		print(''.join(row))

def memoize(grid, startLocation):
    stack = [(startLocation, 0)]
    memo = [[math.inf for _ in row] for row in grid]
    while len(stack) > 0:
        (location, accumulatedCost) = stack.pop()
        memoCost = getValue(memo, location) 
        if accumulatedCost < memoCost:
            setValue(memo, location, accumulatedCost)
            for direction in [NORTH, EAST, SOUTH, WEST]:
                destination = location.move(direction)
                if destination.x < 0 or destination.y < 0 or destination.x >= width or destination.y >= height:
                	continue
                if getValue(grid, destination) != WALL:
                    stack.append((destination, accumulatedCost + 1))
    return memo

def reachable(memo):
    return getValue(memo, Location(width - 1, height - 1)) != math.inf

def apply(grid, events):
    for event in events:
        setValue(grid, event, WALL)

def find(events, start, end):
    if start + 1 == end:
        print(events[start])
        return
    grid = [['.' for _ in range(0, width)] for _ in range(0, height)]
    count = int((start + end) / 2)
    apply(grid, events[0:count])
    memo = memoize(grid, Location(0, 0))
    if not reachable(memo):
        find(events, start, count)
    else:
        find(events, count, end)

find(events, 0, len(events))