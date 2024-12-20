import re

with open("input.txt", "r") as file:
    content = file.read()
regex = r"mul\(([0-9]{0,3}),([0-9]{0,3})\)"

sum = 0
for match in re.finditer(regex, content):
    lhs = match.group(1)
    rhs = match.group(2)
    sum += int(lhs) * int(rhs)
    print(f"Found mul({lhs},{rhs})")
print(sum)