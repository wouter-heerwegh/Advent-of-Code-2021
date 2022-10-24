from typing import List


with open("input.txt") as file:
	lines = file.read().strip().split("\n")

displays = list()
all_numbers = list()
for line in lines:
	all_numbers.append(line.split("|")[0].strip())
	displays.append(line.split("|")[1].strip())

output = list()
for line in displays:
	output.append(line.split(" "))

input = list()
for line in all_numbers:
	input.append(line.split(" "))

solution1 = 0
for line in output:
	for display in line:
		if len(display) == 2 or len(display) == 3 or len(display) == 4 or len(display) == 7:
			solution1 += 1

print(solution1)

def check_nr_of_char_found(number, entry):
	chars_found = 0
	for character in number:
			if character in entry:
				chars_found += 1
	return chars_found

def generate_lookup(data: List):
	input = data.copy()
	numbers = dict()
	done = list()
	while(len(numbers) < 10):
		for entry in input:
			if len(entry) == 2:
				done.append(entry)
				numbers[1] = entry
			elif len(entry) == 3:
				done.append(entry)
				numbers[7] = entry
			elif len(entry) == 4:
				done.append(entry)
				numbers[4] = entry
			elif len(entry) == 7:
				done.append(entry)
				numbers[8] = entry
			elif len(entry) == 5:
				# possibly 2, 3 or 5
				if 1 in numbers:
					# Is it 3?
					if check_nr_of_char_found(numbers[1], entry) == 2:
						done.append(entry)
						numbers[3] = entry
					else:
						if 4 in numbers:
							# Is it 5
							if check_nr_of_char_found(numbers[4], entry) == 3:
								numbers[5] = entry
							else:
								numbers[2] = entry
							done.append(entry)

			elif len(entry) == 6:
				if 4 in numbers:
					# Is it 9?
					if check_nr_of_char_found(numbers[4], entry) == 4:
						done.append(entry)
						numbers[9] = entry
					else:
						if 7 in numbers:
							# Is it 0?
							if check_nr_of_char_found(numbers[7], entry) == 3:
								numbers[0] = entry
							else:
								numbers[6] = entry
								
							done.append(entry)
					
		# remove found entries
		for entry in done:
			input.remove(entry)
		
		done = list()
	return numbers



def compare(item, number):
	if len(item) != len(number):
		return False
	
	for char in number:
		if char not in item:
			return False
	
	return True


sum = 0
for i in range(len(input)):
	lookup = generate_lookup(input[i])

	result = ""
	for item in output[i]:
		nothing_found = True
		for number, segments in lookup.items():
			if compare(item, segments):
				nothing_found = False
				result += str(number)
				break
				
		if nothing_found:
			print("-----------")
			print("Error " + item)
			print(lookup)
	
	sum += int(result)

print(sum)