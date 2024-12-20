with open("input.txt", "r") as file:
	diskMap = file.read().strip()
print(diskMap)

def printMap(diskMap):
	# print(''.join([str(value) for value in diskMap]))
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

lastBlock = len(expandedMap) - 1
while lastBlock > 0 and expandedMap[lastBlock] == '.':
	lastBlock -= 1

nextFreeSpace = 0
while nextFreeSpace < len(expandedMap) and expandedMap[nextFreeSpace] != '.':
	nextFreeSpace += 1

while nextFreeSpace < lastBlock:
	expandedMap[nextFreeSpace] = expandedMap[lastBlock]
	expandedMap[lastBlock] = '.'
	nextFreeSpace += 1
	lastBlock -= 1
	while lastBlock > 0 and expandedMap[lastBlock] == '.':
		lastBlock -= 1
	while nextFreeSpace < len(expandedMap) and expandedMap[nextFreeSpace] != '.':
		nextFreeSpace += 1
printMap(expandedMap)
checksum = 0
for i in range(len(expandedMap)):
	if expandedMap[i] == '.':
		break
	checksum += i * int(expandedMap[i])
print(checksum)