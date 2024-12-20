GUARD_UP = "^"
GUARD_LEFT = "<"
GUARD_RIGHT = ">"
GUARD_DOWN = "V"
GUARD_ANY = set([GUARD_UP, GUARD_LEFT, GUARD_RIGHT, GUARD_DOWN])
EMPTY = "."
OBSTACLE = "#"

with open("input.txt", "r") as file:
    board = [list(line.strip()) for line in file]
height = len(board)
width = len(board[0])

def valueAt(board, position):
    return board[position[1]][position[0]]

def setValueAt(board, value, position):
    board[position[1]][position[0]] = value

def addMemory(memory, value, position):
    memory[position[1]][position[0]].add(value)

def isGuardOffMap(guardPosition):
    if guardPosition[0] < 0 or guardPosition[0] == width:
        return True
    if guardPosition[1] < 0 or guardPosition[1] == height:
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

def calculateNextGuardPosition(board, guardPosition):
    guardValue = valueAt(board, guardPosition)
    if guardValue == GUARD_UP:
        return (guardPosition[0], guardPosition[1] - 1)
    if guardValue == GUARD_RIGHT:
        return (guardPosition[0] + 1, guardPosition[1])
    if guardValue == GUARD_DOWN:
        return (guardPosition[0], guardPosition[1] + 1)
    if guardValue == GUARD_LEFT:
        return (guardPosition[0] - 1, guardPosition[1])
    return False

def runSimulationAndDetectCycle(board):
    # Find the initial guard position
    guardPosition = (0, 0)
    for y, row in enumerate(board):
        for x, tile in enumerate(row):
            if tile in GUARD_ANY:
                guardPosition = (x, y)
    memory = [[set() for _ in range(width)] for _ in range(height)]
    while True:
        guardValue = valueAt(board, guardPosition)
        if guardValue in valueAt(memory, guardPosition):
            return True
        addMemory(memory, guardValue, guardPosition)
        nextGuardPosition = calculateNextGuardPosition(board, guardPosition)
        if isGuardOffMap(nextGuardPosition):
            return False
        nextValue = valueAt(board, nextGuardPosition)
        if nextValue == OBSTACLE:
            setValueAt(board, rotateRight(guardValue), guardPosition)
        else:
            setValueAt(board, EMPTY, guardPosition)
            setValueAt(board, guardValue, nextGuardPosition)
            guardPosition = nextGuardPosition

count = 0
for j, row in enumerate(board):
    for i, candidateValue in enumerate(row):
        if candidateValue != EMPTY:
            print(f"skipping ({i}, {j})")
            continue
        print(f"checking ({i}, {j})")
        candidateBoard = [row[:] for row in board]
        setValueAt(candidateBoard, OBSTACLE, (i, j))
        if runSimulationAndDetectCycle(candidateBoard):
            count += 1

print(count)

