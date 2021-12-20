from parse import parse


class Coord(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def print(self):
		print(str(self.x) + ", " + str(self.y))



with open("input.txt") as file:
	lines = file.read().splitlines()

coords = []

largest_x = 0
largest_y = 0

for line in lines:
	parsed = parse("{:d},{:d} -> {:d},{:d}", line)

	if parsed[0] > largest_x or parsed[2] > largest_x:
		largest_x = max(parsed[0], parsed[2])

	if parsed[1] > largest_y or parsed[3] > largest_y:
		largest_y = max(parsed[1], parsed[3])

	coord1 = Coord(parsed[0], parsed[1])
	coord2 = Coord(parsed[2], parsed[3])
	coords.append([coord1, coord2])

board= [[0 for x in range(largest_x + 1)] for y in range(largest_y + 1)]

for path in coords:
	if path[0].x == path[1].x:
		start = min(path[0].y, path[1].y)
		end = max(path[0].y, path[1].y) + 1
		for j in range(start, end):
			board[j][path[0].x] += 1
	elif path[0].y == path[1].y:
		start = min(path[0].x, path[1].x)
		end = max(path[0].x, path[1].x) + 1
		for i in range(start, end):
			board[path[0].y][i] += 1

counter = 0
for line in board:
	for cell in line:
		if cell > 1:
			counter += 1

print(counter)

board = [[0 for x in range(largest_x + 1)] for y in range(largest_y + 1)]

increment_x = 1
increment_y = 1

for path in coords:
	if path[0].x >= path[1].x:
		increment_x = -1
	else:
		increment_x = 1
	
	if path[0].y >= path[1].y:
		increment_y = -1
	else:
		increment_y = 1

	x = path[0].x
	y = path[0].y
	while True:
		board[y][x] += 1
		if x == path[1].x and y == path[1].y:
			break


		if x != path[1].x:
			x += increment_x

		if y != path[1].y:
			y += increment_y

counter = 0
for line in board:
	for cell in line:
		if cell > 1:
			counter += 1

print(counter)