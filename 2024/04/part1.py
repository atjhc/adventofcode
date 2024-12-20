

text = "XMAS"
textLength = len(text)
with open("input.txt", "r") as file:
    board = [list(line.strip()) for line in file]
height = len(board)
width = len(board[0])

print(f"width={width}, height={height}")

def checkMatch(x, y, dx, dy):
    ex = x + dx * (textLength - 1)
    if ex < 0 or ex >= width:
        return False
    ey = y + dy * (textLength - 1)
    if ey < 0 or ey >= height:
        return False
    for i in range(0, textLength):
        if board[y][x] != text[i]:
            return False
        x += dx
        y += dy
    return True

matches = 0
for j in range(0, height):
    matchesInLine = 0
    for i in range(0, width):
        if checkMatch(i, j,  0,  1): matches += 1
        if checkMatch(i, j,  1,  1): matches += 1
        if checkMatch(i, j,  1,  0): matches += 1
        if checkMatch(i, j,  1, -1): matches += 1
        if checkMatch(i, j,  0, -1): matches += 1
        if checkMatch(i, j, -1, -1): matches += 1
        if checkMatch(i, j, -1,  0): 
            matches += 1
            matchesInLine += 1
        if checkMatch(i, j, -1,  1): matches += 1
    print(f"{j + 1}: {matchesInLine}")
print(f"matches={matches}")