import re

text = "XMAS"
textLength = len(text)
with open("input.txt", "r") as file:
    board = [list(line.strip()) for line in file]
height = len(board)
width = len(board[0])

patterns =[['M.S',
            '.A.',
            'M.S'],
           ['S.S',
            '.A.',
            'M.M'],
           ['M.M',
            '.A.',
            'S.S'],
           ['S.M',
            '.A.',
            'S.M']]

def checkMatch(x, y, pattern):
    for line in pattern:
        substring = ''.join(board[y][x:x + len(line)])
        if not re.compile(line).search(substring):
            return False
        y += 1
    return True

matches = 0
for y in range(0, height - 2):
    for x in range(0, width - 2):
        for pattern in patterns:
            if checkMatch(x, y, pattern):
                matches += 1
                continue
print(matches)