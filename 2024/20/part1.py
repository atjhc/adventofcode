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

def show(maze):
    for row in maze:
        print(''.join(row))

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

def solve(memo, startLocation, endLocation):
    locations = []
    currentLocation = endLocation
    while currentLocation != startLocation:
        locations.append(currentLocation)
        currentCost = getValue(memo, currentLocation)
        previousLocation = currentLocation
        for direction in [NORTH, EAST, SOUTH, WEST]:
            nextLocation = currentLocation.move(direction)
            if getValue(memo, nextLocation) == currentCost - 1:
                currentLocation = nextLocation
                break
        if currentLocation == previousLocation:
            break
    locations.append(startLocation)
    locations.reverse()
    return locations

def overlay(data, locations, value):
    for location in locations:
        setValue(data, location, value)

def copy(data):
    return [row[:] for row in data]

def findValue(data, value):
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v == value:
                return Location(x, y)
    return None

startLocation = findValue(maze, START)
endLocation = findValue(maze, END)
memo = memoize(maze, startLocation)
baseCost = getValue(memo, endLocation)

count = 0
for y, row in enumerate(maze):
    for x, value in enumerate(row):
        if value == WALL:
            continue
        location = Location(x, y)
        currentCost = getValue(memo, location)
        for direction in [NORTH, EAST, SOUTH, WEST]:
            cheatLocation = location.move(direction, 2)
            if not cheatLocation.inBounds() or getValue(maze, cheatLocation) == WALL:
                continue
            cheatMemo = copy(memo)
            memoize(maze, cheatLocation, currentCost + 2, cheatMemo)
            cheatCost = getValue(cheatMemo, endLocation)
            if cheatCost < baseCost:
                savings = baseCost - cheatCost
                if savings >= 100:
                    count += 1
print(count)