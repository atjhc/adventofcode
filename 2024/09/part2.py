from dataclasses import dataclass

@dataclass
class Range:
    location: int
    length: int

with open("input.txt", "r") as file:
	diskMap = file.read().strip()
print(diskMap)

def printMap(diskMap):
	print(diskMap)
	pass

expandedMap = []
ID = 0
i = 0
while i < len(diskMap):
	blockSize = int(diskMap[i])
	expandedMap += blockSize * [ID]
	ID += 1
	if i + 1 < len(diskMap):
		spaceSize = int(diskMap[i+1])
		expandedMap += spaceSize * "."
	i += 2

printMap(expandedMap)

def findNextFile(diskMap, currentFile):
	nextFile = Range(currentFile.location, 0)
	if nextFile.location == 0:
		return None
	nextFile.location -= 1
	while nextFile.location > 0 and diskMap[nextFile.location] == '.':
		nextFile.location -= 1
	ID = diskMap[nextFile.location]
	endLocation = nextFile.location + 1
	while nextFile.location - 1 > 0 and diskMap[nextFile.location - 1] == ID:
		nextFile.location -= 1
	nextFile.length = endLocation - nextFile.location
	return nextFile

def findNextSpace(diskMap, currentSpace):
	nextSpace = Range(currentSpace.location + currentSpace.length, 0)
	while nextSpace.location < len(diskMap) and diskMap[nextSpace.location] != '.':
		nextSpace.location += 1
	endLocation = nextSpace.location
	while endLocation < len(diskMap) and diskMap[endLocation] == '.':
		endLocation += 1
	nextSpace.length = endLocation - nextSpace.location
	return nextSpace

def findSpaceWithLength(diskMap, length):
	currentSpace = findNextSpace(expandedMap, Range(0, 0))
	while currentSpace.length > 0 and currentSpace.length < length:
		currentSpace = findNextSpace(expandedMap, currentSpace)
	return currentSpace

currentFile = findNextFile(expandedMap, Range(len(expandedMap), 0))
while currentFile.location > 0:
	print(currentFile)
	space = findSpaceWithLength(expandedMap, currentFile.length)
	if space.location < currentFile.location:
		for i in range(currentFile.length):
			expandedMap[space.location + i] = expandedMap[currentFile.location + i]
			expandedMap[currentFile.location + i] = '.'
	currentFile = findNextFile(expandedMap, currentFile)

printMap(expandedMap)
checksum = 0
for i in range(len(expandedMap)):
	if expandedMap[i] == '.':
		continue
	checksum += i * int(expandedMap[i])
print(checksum)