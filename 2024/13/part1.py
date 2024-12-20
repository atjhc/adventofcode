class Machine:
	def __init__(self, buttonA, buttonB, prize):
		self.buttonA = buttonA
		self.buttonB = buttonB
		self.prize = prize

machines = []
with open("input.txt", "r") as file:
	def readButton(line):
		parts = line.strip().split(':')[1].split(',')
		return (int(parts[0][3:]), int(parts[1][3:]))
		
	while True:
		buttonA = readButton(file.readline())
		buttonB = readButton(file.readline())
		parts = file.readline().strip().split(':')[1].split(',')
		prize = (int(parts[0][3:]), int(parts[1][3:]))
		machines.append(Machine(buttonA, buttonB, prize))
		if file.readline() == '':
			break

total = 0
for i, machine in enumerate(machines):
	smallest = None
	print(f"machine {i}")
	for a in range(101):
		for b in range(101):
			location = (machine.buttonA[0] * a + machine.buttonB[0] * b, machine.buttonA[1] * a + machine.buttonB[1] * b)
			if location[0] == machine.prize[0] and location[1] == machine.prize[1]:
				cost = 3 * a + b
				if smallest == None or cost < smallest:
					smallest = cost
	if smallest != None:
		total += smallest
print(total)
