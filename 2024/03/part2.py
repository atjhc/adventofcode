import re

with open("input.txt", "r") as file:
    content = file.read()
regex = r"do\(\)|don't\(\)|mul\(([0-9]{0,3}),([0-9]{0,3})\)"

sum = 0
enabled = True
for match in re.finditer(regex, content):
    command = match.group(0)
    if command == "do()":
        enabled = True
        continue
    if command == "don't()":
        enabled = False
        continue
    if not enabled:
        continue
    print(command)
    lhs = match.group(1)
    rhs = match.group(2)
    sum += int(lhs) * int(rhs)
    print(f"Found mul({lhs},{rhs})")
print(sum)