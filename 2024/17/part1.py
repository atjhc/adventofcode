class VM:
	def __init__(self, registerA, registerB, registerC, program):
		self.registerA = registerA
		self.registerB = registerB
		self.registerC = registerC
		self.program = program
		self.IP = 0
		self.out = []
		self.debug = False

	def combo(self, operand):
		match operand:
			case _ if 0 <= operand <= 3:
				return operand
			case 4:
				return self.registerA
			case 5:
				return self.registerB
			case 6:
				return self.registerC
		return None

	def execute(self, opcode, operand):
		match opcode:
			case 0: # adv
				self.registerA = int(self.registerA / (2 ** self.combo(operand)))
			case 1: # bxl
				self.registerB = self.registerB ^ operand
			case 2: # bst
				self.registerB = self.combo(operand) % 8
			case 3: # jnz
				if self.registerA != 0:
					self.IP = operand
					return
			case 4: # bxc
				self.registerB = self.registerB ^ self.registerC
			case 5: # out
				self.out.append(self.combo(operand) % 8)
			case 6: # bdv
				self.registerB = int(self.registerA / (2 ** self.combo(operand)))
			case 7: # cdv
				self.registerC = int(self.registerA / (2 ** self.combo(operand)))
		self.IP += 2

	def run(self):
		while self.IP < len(self.program):
			if self.debug:
				print(f"Register A: {self.registerA}")
				print(f"Register B: {self.registerB}")
				print(f"Register C: {self.registerC}")
				print(f"IP: {self.IP}")
				print(f"Out: {self.out}")
				print("-")
			self.execute(self.program[self.IP], self.program[self.IP + 1])

with open("test4.txt") as file:
	a = int(file.readline().strip().split(": ")[1])
	b = int(file.readline().strip().split(": ")[1])
	c = int(file.readline().strip().split(": ")[1])
	file.readline()
	p = file.readline().strip().split(": ")[1].split(",")
	vm = VM(a, b, c, [int(code) for code in p])

vm.run()
print(','.join([str(v) for v in vm.out]))