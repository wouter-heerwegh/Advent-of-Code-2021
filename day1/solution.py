with open("input.txt") as file:
	lines = file.read().splitlines()

prev = int(lines[0])
counter = 0
for depth in lines:
	if int(depth) > prev:
		counter += 1
	prev = int(depth)

print(counter)

values = []
for val in lines:
	values.append(int(val))

counter = 0

prev_sum = sum = values[0] + values[1] + values[2]
for i in range(len(values)-2):
	sum = values[i] + values[i + 1] + values[i + 2]

	if(sum > prev_sum):
		counter += 1
	prev_sum = sum

print(counter)