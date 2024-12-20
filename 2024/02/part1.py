safeCount = 0
with open("input.txt", "r") as file:
    for line in file:
        input = map(int, line.split())
        previousNumber = None
        previousDirection = None
        isGood = True
        for number in input:
            # If this is the first number
            if previousNumber is None:
                previousNumber = number
                continue
            difference = number - previousNumber
            # Number is not changing
            if difference == 0:
                isGood = False
                break
            direction = -1 if difference < 0 else 1
            # If this is the second number
            if previousDirection is None:
                previousDirection = direction
            else:
                # If the direction has changed
                if previousDirection != direction:
                    isGood = False
                    break
            if abs(difference) > 3:
                isGood = False
                break
            previousNumber = number
        if isGood:
            safeCount += 1
print(safeCount)