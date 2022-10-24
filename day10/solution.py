import math


opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']

lookup = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}

with open("input.txt") as file:
	lines = file.read().splitlines()

incomplete_lines = list()
sum = 0
for line in lines:
	stack = []
	error_found = False
	for char in line:
		if char in opening:
			stack.append(char)
		elif char in closing:
			if opening.index(stack[-1]) == closing.index(char):
				# closing chunck correctly
				stack.pop()
			else:
				error_found = True
				print("Error")
				print(str(stack[-1]) + " but got " + char)
				sum += lookup[char]
				break

	if len(stack) > 0 and not error_found:
		print("Stack not empty --> incomplete")
		incomplete_lines.append(stack)

print(sum)

scores = list()
for line in incomplete_lines:
	score = 0
	closing_chunks = ""
	while len(line) > 0:
		char = line.pop()
		score *= 5
		score += opening.index(char) + 1
	scores.append(score)
	
scores.sort()
print(scores[math.floor(len(scores)/2)])