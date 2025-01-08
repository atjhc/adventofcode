import math

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

WALL = '#'
START = 'S'
END = 'E'

with open("input.txt") as file:
    maze = [list(row.strip()) for row in file]
height = len(maze)
width = len(maze[0])

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def north(self, distance=1):
        return Location(self.x, self.y - distance)

    def east(self, distance=1):
        return Location(self.x + distance, self.y)

    def south(self, distance=1):
        return Location(self.x, self.y + distance)

    def west(self, distance=1):
        return Location(self.x - distance, self.y)

    def move(self, direction, distance=1):
        funcs = [self.north, self.east, self.south, self.west]
        return funcs[direction](distance)

    def inBounds(self):
        return self.x >= 0 and self.y >= 0 and self.x < width and self.y < height

    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def getValue(data, location):
    return data[location.y][location.x]

def setValue(data, location, value):
    data[location.y][location.x] = value

def memoize(maze, startLocation, startCost=0, memo=None):
    if memo == None:
        memo = [[math.inf for _ in row] for row in maze]
    stack = [(startLocation, startCost)]
    while len(stack) > 0:
        (location, accumulatedCost) = stack.pop()
        memoCost = getValue(memo, location) 
        if accumulatedCost < memoCost:
            setValue(memo, location, accumulatedCost)
            for direction in [NORTH, EAST, SOUTH, WEST]:
                destination = location.move(direction)
                if not destination.inBounds():
                    continue
                if getValue(maze, destination) != WALL:
                    stack.append((destination, accumulatedCost + 1))
    return memo

def findValue(data, value):
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v == value:
                return Location(x, y)
    return None

offsets = []
for x in range(-20, 21):
    for y in range(-20, 21):
        if abs(x) + abs(y) <= 20:
            offsets.append((x, y))

memo = memoize(maze, findValue(maze, END))

count = 0
for y, row in enumerate(maze):
    for x, value in enumerate(row):
        if value == WALL:
            continue
        location = Location(x, y)
        currentCost = getValue(memo, location)
        for offset in offsets:
            cheatLocation = Location(location.x + offset[0], location.y + offset[1])
            if not cheatLocation.inBounds() or getValue(maze, cheatLocation) == WALL:
                continue
            delta = currentCost - (getValue(memo, cheatLocation) + abs(offset[0]) + abs(offset[1]))
            if delta >= 100:
                count += 1
print(count)
