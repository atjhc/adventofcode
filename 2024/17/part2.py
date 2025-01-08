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
				# self.registerB = int(self.registerA / (2 ** self.combo(operand)))
				self.registerB = self.registerA >> self.combo(operand)
			case 7: # cdv
				# self.registerC = int(self.registerA / (2 ** self.combo(operand)))
				self.registerC = self.registerA >> self.combo(operand)
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

with open("input.txt") as file:
	a = int(file.readline().strip().split(": ")[1])
	b = int(file.readline().strip().split(": ")[1])
	c = int(file.readline().strip().split(": ")[1])
	file.readline()
	p = file.readline().strip().split(": ")[1].split(",")
	vm = VM(a, b, c, [int(code) for code in p])

# There was no special magic to finding these digits. I manually worked them out from most significant
# to least significant, since I noticed the program was shifting 3 bits off A after every step, so I
# split it into 3 bit chunks, and tried different values that seemed to produce the correct sequence.
# I reasoned that given there are 16 values in the output, we should have about 3*16 = 48 bits in our
# final value. Parts of the program I used to work out chunks of these digits is commented out below.
# I found them manually until I had enough that I could find the remaining through brute force.
digits = [0b110, 0b101, 0b110, 0b010, 0b010, 0b101, 0b111, 0b100, 0b000, 0b100, 0b010, 0b101, 0b111]

a = 0
for i, digit in enumerate(digits):
	a = a | digit << (45 - i*3) 

while True:
	vm.registerA = a
	vm.registerB = 0
	vm.registerC = 0
	vm.out = []
	vm.IP = 0
	vm.run()
	if vm.program == vm.out:
		print(a)
		break
	a += 1