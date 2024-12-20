from decimal import Decimal, getcontext
getcontext().prec = 100

CONVERSION = 10000000000000

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
		prize = (CONVERSION + int(parts[0][3:]), CONVERSION + int(parts[1][3:]))
		machines.append(Machine(buttonA, buttonB, prize))
		if file.readline() == '':
			break

def decimal(tuple):
	return (Decimal(tuple[0]), Decimal(tuple[1]))

total = 0
for machine in machines:
	# (x1, y1) = machine.buttonA
	# (x2, y2) = machine.buttonB
	# (x3, y3) = machine.prize
	(x1, y1) = decimal(machine.buttonA)
	(x2, y2) = decimal(machine.buttonB)
	(x3, y3) = decimal(machine.prize)
	a = (x3 - (y3 * x2) / y2) / (x1 - (y1 * x2) / y2)
	b = (y3 - a * y1) / y2
	a = a.quantize(Decimal(1))
	b = b.quantize(Decimal(1))
	if a < 0 or b < 0:
		continue
	if a * x1 + b * x2 != x3 or a * y1 + b * y2 != y3:
		print(f"SKIP: {(a, b)} -> {(a * x1 + b * x2, a * y1 + b * y2)}")	
		continue
	a = int(a)
	b = int(b)
	print(f"KEEP: {(a, b)} -> {(a * x1 + b * x2, a * y1 + b * y2)}")	
	total += 3 * a + b

print(total)
