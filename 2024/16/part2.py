import math
import sys

# # Set a new recursion limit
# sys.setrecursionlimit(10000)

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

    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

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

def backtrack(memo, startLocation, endLocation):
    tiles = [[None for _ in row] for row in memo]
    stack = [(endLocation, None)]
    while len(stack) > 0:
        (location, facing) = stack.pop()
        debugPrint(tiles, maze)
        print((location, facing))
        if getValue(tiles, location) != 'O':
            setValue(tiles, location, 'O')
            if location == startLocation:
                continue
            costs = []
            for direction, cost in enumerate(getValue(memo, location)):
                if facing == None:
                    (_, rotateCost) = location.move(OPPOSITES[direction], direction)
                else:
                    (_, rotateCost) = location.move(facing, direction)
                costs.append(cost + rotateCost)
            minCost = min(costs)
            if minCost == 0:
                continue
            for direction, cost in enumerate(costs):
                (destination, _) = location.move(OPPOSITES[direction], direction)
                if cost == minCost:
                    stack.append((destination, direction))
    return tiles


def search(location, facing, accumulatedCost):
    value = getValue(maze, location)
    memoCost = getValue(memo, location)
    if memoCost[facing] < accumulatedCost:
        return memoCost[facing]
    memoCost[facing] = accumulatedCost
    debugPrint(memo)
    if value == 'E':
        return memoCost[facing]
    for direction in [NORTH, EAST, SOUTH, WEST]:
        if OPPOSITES[direction] == facing:
            continue
        (destination, rotateCost) = location.move(direction, facing)
        if getValue(maze, destination) != '#':
            search(destination, direction, accumulatedCost + rotateCost + MOVE_COST)
    return memoCost[facing]

def findValue(data, value):
    for y, row in enumerate(data):
        for x, candidate in enumerate(row):
            if candidate == value:
                return Location(x, y)
    return None

def debugPrint(tiles, maze):
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            if tile == 'O':
                print('O', end='')
            else:
                print(getValue(maze, Location(x, y)), end='')
        print('')

startLocation = findValue(maze, 'S')
endLocation = findValue(maze, 'E')
memo = memoize(maze, startLocation, EAST)
print(getValue(memo, endLocation))
print(getValue(memo, Location(5, 7)))
tiles = backtrack(memo, startLocation, endLocation)

total = 0
for y, row in enumerate(tiles):
    for x, tile in enumerate(row):
        if tile == 'O':
            print('O', end='')
            total += 1
        else:
            print(getValue(maze, Location(x, y)), end='')
    print('')
print(total)
