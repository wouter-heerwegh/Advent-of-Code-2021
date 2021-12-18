from parse import parse

with open("input.txt") as file:
	lines = file.read().splitlines()

hor = 0
depth = 0
for op in lines:
	if "forward" in op:
		hor += int(parse("forward {}", op)[0])
	elif "down" in op:
		depth += int(parse("down {}", op)[0])
	elif "up" in op:
		depth -= int(parse("up {}", op)[0])

print(hor * depth)


hor = 0
aim = 0
depth = 0
for op in lines:
	if "forward" in op:
		hor += int(parse("forward {}", op)[0])
		depth += int(parse("forward {}", op)[0]) * aim
	elif "down" in op:
		aim += int(parse("down {}", op)[0])
	elif "up" in op:
		aim -= int(parse("up {}", op)[0])

print(hor * depth)