import math

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
ROTATE_COST = 1000
MOVE_COST = 1
OPPOSITES = [SOUTH, WEST, NORTH, EAST]

with open("input.txt") as file:
    maze = [list(row.strip()) for row in file]

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def north(self, direction):
        return (Location(self.x, self.y - 1), [0, ROTATE_COST, ROTATE_COST * 2, ROTATE_COST][direction])

    def east(self, direction):
        return (Location(self.x + 1, self.y), [ROTATE_COST, 0, ROTATE_COST, ROTATE_COST * 2][direction])

    def south(self, direction):
        return (Location(self.x, self.y + 1), [ROTATE_COST * 2, ROTATE_COST, 0, ROTATE_COST][direction])

    def west(self, direction):
        return (Location(self.x - 1, self.y), [ROTATE_COST, ROTATE_COST * 2, ROTATE_COST, 0][direction])

    def move(self, toDirection, fromDirection):
        funcs = [self.north, self.east, self.south, self.west]
        return funcs[toDirection](fromDirection)

    def __repr__(self):
        return f"({x}, {y})"

def getValue(data, location):
    return data[location.y][location.x]

def setValue(data, location, value):
    data[location.y][location.x] = value

def memoize(maze, location, facing):
    stack = [(location, facing, 0)]
    memo = [[[math.inf, math.inf, math.inf, math.inf] for _ in row] for row in maze]
    while len(stack) > 0:
        (location, facing, accumulatedCost) = stack.pop()
        memoCost = getValue(memo, location) 
        if accumulatedCost < memoCost[facing]:
            memoCost[facing] = accumulatedCost
            for direction in [NORTH, EAST, SOUTH, WEST]:
                if OPPOSITES[direction] == facing:
                    continue
                (destination, rotateCost) = location.move(direction, facing)
                if getValue(maze, destination) != '#':
                    stack.append((destination, direction, accumulatedCost + rotateCost + MOVE_COST))
    return memo

def findValue(data, value):
    for y, row in enumerate(data):
        for x, candidate in enumerate(row):
            if candidate == value:
                return Location(x, y)
    return None

startLocation = findValue(maze, 'S')
endLocation = findValue(maze, 'E')
memo = memoize(maze, startLocation, EAST)
print(min(getValue(memo, endLocation)))
