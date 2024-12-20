import time
from collections import deque

cache = {}

class CachedValues:
    def __init__(self, values):
        self.values = values
        self.count = count(values)

class Reference:
    def __init__(self, value, generation):
        self.value = value
        self.generation = generation

def getCache(reference):
    if reference.value not in cache:
        return None
    values = cache[reference.value]
    return values.get(reference.generation)

def setCache(reference, values):
    if reference.value not in cache:
        cache[reference.value] = {}
    cache[reference.value][reference.generation] = values

def step(stones):
    result = []
    for stone in stones:
        if isinstance(stone, Reference):
            newStone = Reference(stone.value, stone.generation + 1)
            cachedValues = getCache(newStone)
            if cachedValues == None:
                cachedValues = getCache(stone)
                setCache(newStone, CachedValues(step(cachedValues.values)))
            result.append(newStone)
        elif stone == 0:
            result.append(1)
        else:
            digits = str(stone)
            if len(digits) % 2 == 0:
                reference = Reference(stone, 1)
                newStone = getCache(reference)
                if newStone == None:
                    left = int(digits[0:len(digits) // 2])
                    right = int(digits[len(digits) // 2 : len(digits)])
                    setCache(reference, CachedValues([left, right]))
                result.append(reference)
            else:
                result.append(stone * 2024)
    return result

def count(stones):
    total = 0
    for stone in stones:
        if isinstance(stone, Reference):
            total += getCache(stone).count
        else:
            total += 1
    return total

with open("input.txt", "r") as file:
     stones = deque([int(value) for value in file.read().strip().split()])
blinks = 75

for i in range(blinks):
    startTime = time.time()
    stones = step(stones)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"{elapsedTime:.2f} Completed step {i}")
print(count(stones))