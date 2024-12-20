from collections import namedtuple
Location = namedtuple('Location', ['x', 'y'])

class Board:
    @classmethod
    def fromFile(cls, file_path):
        with open(file_path, 'r') as file:
            data = [list(line.strip()) for line in file]
        height = len(data)
        width = len(data[0]) if height > 0 else 0
        instance = cls(width, height, None)
        instance.data = data
        return instance

    def __init__(self, width, height, defaultValue=None):
        self.data = [[defaultValue for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height

    def value(self, location):
        return self.data[location.y][location.x]

    def setValue(self, location, value):
        self.data[location.y][location.x] = value

    def slope(self, location1, location2):
        return int(self.value(location2)) - int(self.value(location1))

    def inBounds(self, location):
        if location.x < 0 or location.x >= self.width:
            return False
        if location.y < 0 or location.y >= self.height:
            return False
        return True

    def __repr__(self):
        return '\n'.join([''.join(map(str, row)) for row in self.data])

VISITED = "X"
FOUND = "O"

board = Board.fromFile("input.txt")

def search(board, memo, location):
    if memo.value(location) == VISITED:
        return
    if board.value(location) == '9':
        memo.setValue(location, FOUND)
        return
    memo.setValue(location, VISITED)
    north = Location(location.x, location.y - 1)
    if board.inBounds(north) and board.slope(location, north) == 1:
        search(board, memo, north)
    east = Location(location.x + 1, location.y)
    if board.inBounds(east) and board.slope(location, east) == 1:
        search(board, memo, east)
    south = Location(location.x, location.y + 1)
    if board.inBounds(south) and board.slope(location, south) == 1:
        search(board, memo, south)
    west = Location(location.x - 1, location.y)
    if board.inBounds(west) and board.slope(location, west) == 1:
        search(board, memo, west)

def countFound(memo):
    count = 0
    for row in memo.data:
        for value in row:
            if value == FOUND:
                count += 1
    return count

total = 0
for y, row in enumerate(board.data):
    for x, value in enumerate(row):
        if value == '0':
            memo = Board(board.width, board.height, defaultValue='.')
            search(board, memo, Location(x, y))
            found = countFound(memo)
            print(memo)
            print(found)
            total += countFound(memo)
print(total)