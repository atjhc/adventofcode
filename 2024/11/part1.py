import time
from collections import deque

with open("input.txt", "r") as file:
     stones = deque([int(value) for value in file.read().strip().split()])

def step(stones):
    result = deque()
    for stone in stones:
        if stone == 0:
            result.append(1)
        else:
            digits = str(stone)
            if len(digits) % 2 == 0:
                left = digits[0:len(digits) // 2]
                right = digits[len(digits) // 2 : len(digits)]
                result.append(int(left))
                result.append(int(right))
            else:
                result.append(stone * 2024)
    return result

blinks = 25
for i in range(blinks):
    startTime = time.time()
    stones = step(stones)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"{elapsedTime:.2f} Completed step {i}: {len(stones)}")