GUARD_UP = "^"
GUARD_LEFT = "<"
GUARD_RIGHT = ">"
GUARD_DOWN = "V"
GUARD_ANY = set([GUARD_UP, GUARD_LEFT, GUARD_RIGHT, GUARD_DOWN])
EMPTY = "."
EMPTY_VISITED = "X"
EMPTY_ANY = set([EMPTY, EMPTY_VISITED])
OBSTACLE = "#"

with open("input.txt", "r") as file:
    board = [list(line.strip()) for line in file]
height = len(board)
width = len(board[0])

# Find the initial guard position
guardPosition = (0, 0)
for y, row in enumerate(board):
    for x, tile in enumerate(row):
        if tile in GUARD_ANY:
            guardPosition = (x, y)
            print(f"found guard at {guardPosition}")

def valueAt(position):
    return board[position[1]][position[0]]

def setValueAt(value, position):
    board[position[1]][position[0]] = value

def isGuardOffMap(guardPosition):
    if nextGuardPosition[0] < 0 or nextGuardPosition[0] == width:
        return True
    if nextGuardPosition[1] < 0 or nextGuardPosition[1] == height:
        return True
    return False

def rotateRight(guardValue):
    if guardValue == GUARD_UP:
        return GUARD_RIGHT
    if guardValue == GUARD_RIGHT:
        return GUARD_DOWN
    if guardValue == GUARD_DOWN:
        return GUARD_LEFT
    if guardValue == GUARD_LEFT:
        return GUARD_UP
    return guardValue

def calculateNextGuardPosition(guardPosition):
    guardValue = valueAt(guardPosition)
    print(guardValue)
    if guardValue == GUARD_UP:
        return (guardPosition[0], guardPosition[1] - 1)
    if guardValue == GUARD_RIGHT:
        return (guardPosition[0] + 1, guardPosition[1])
    if guardValue == GUARD_DOWN:
        return (guardPosition[0], guardPosition[1] + 1)
    if guardValue == GUARD_LEFT:
        return (guardPosition[0] - 1, guardPosition[1])
    return False

while True:
    nextGuardPosition = calculateNextGuardPosition(guardPosition)
    if isGuardOffMap(nextGuardPosition):
        break
    guardValue = valueAt(guardPosition)
    nextValue = valueAt(nextGuardPosition)
    if nextValue == OBSTACLE:
        setValueAt(rotateRight(guardValue), guardPosition)
    else:
        setValueAt(EMPTY_VISITED, guardPosition)
        setValueAt(guardValue, nextGuardPosition)
        guardPosition = nextGuardPosition

# Start at one for the ending guard position
count = 1
for row in board:
    print(f"{''.join(row)}")
    for value in row:
        if value == EMPTY_VISITED:
            count += 1
print(count)

