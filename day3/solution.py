with open("input.txt") as file:
	lines = file.read().splitlines()


gamma = ""

for i in range(len(lines[0])):
	counter = 0
	for line in lines:
		if line[i] == '1':
			counter += 1
	
	if counter >= len(lines)/2:
		gamma += '1'
	else:
		gamma += '0'

epsilon = ""
for char in gamma:
	if char == '1':
		epsilon += '0'
	else:
		epsilon += '1'

print(str(int(gamma, 2) * int(epsilon, 2)))

def get_most_common_bit(data, index):
	counter = 0
	for line in data:
		if line[index] == '1':
			counter += 1
	
	if counter >= len(data)/2:
		return '1'
	
	return '0'


oxy = ""
scrub = ""

resulting_list = lines.copy()

for i in range(len(lines[0])):
	data = resulting_list.copy()
	resulting_list.clear()
	bit = get_most_common_bit(data, i)
	for line in data:
		if line[i] == bit:
			resulting_list.append(line)
	if len(resulting_list) == 1:
		break

oxy = resulting_list[0]

resulting_list = lines

for i in range(len(lines[0])):
	data = resulting_list.copy()
	resulting_list.clear()
	bit = get_most_common_bit(data, i)
	for line in data:
		if line[i] != bit:
			resulting_list.append(line)
	if len(resulting_list) == 1:
		break

scrub = resulting_list[0]

print(int(oxy,2) * int(scrub,2))