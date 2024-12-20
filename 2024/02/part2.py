def checkIsSafe(input):
    previousNumber = None
    previousDirection = None
    isSafe = True
    for number in input:
        # If this is the first number
        if previousNumber is None:
            previousNumber = number
            continue
        difference = number - previousNumber
        # Number is not changing
        if difference == 0:
            isSafe = False
            break
        direction = -1 if difference < 0 else 1
        # If this is the second number
        if previousDirection is None:
            previousDirection = direction
        else:
            # If the direction has changed
            if previousDirection != direction:
                isSafe = False
                break
        if abs(difference) > 3:
            isSafe = False
            break
        previousNumber = number
    return isSafe


safeCount = 0
with open("input.txt", "r") as file:
    for line in file:
        input = list(map(int, line.split()))
        if checkIsSafe(input):
            safeCount += 1
        else:
            isSafe = False
            for i in range(len(input)):
                if checkIsSafe(input[:i] + input[i+1:]):
                    isSafe = True
                    break
            if isSafe:
                safeCount += 1
print(safeCount)