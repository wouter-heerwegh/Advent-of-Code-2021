from dataclasses import dataclass

@dataclass
class Coordinate:
	x: int
	y: int
	
directions = list()
directions.append(Coordinate(0, -1)) # left
directions.append(Coordinate(-1, 0)) # up
directions.append(Coordinate(0, 1)) # right
directions.append(Coordinate(1, 0)) # down

with open("input.txt") as file:
	lines = file.read().splitlines()

low_points = list()
for i in range(len(lines)):
	for j in range(len(lines[0])):
		low_point = True
		for direction in directions:
			if i + direction.x < 0 or j + direction.y < 0 or i + direction.x >= len(lines) or j + direction.y >= len(lines[0]):
				continue
			
			if lines[i][j] >= lines[i + direction.x][j + direction.y]:
				low_point = False
		
		if low_point:
			low_points.append(Coordinate(i, j))

solution1 = 0
for low_point in low_points:
	solution1 += int(lines[low_point.x][low_point.y]) + 1
	
print(solution1)

visited = [[False for j in range(len(lines[0]))] for i in range(len(lines))]

def recursive_explore(data, visited, coord):
	count = 1
	for direction in directions:
		# Check bounds
		if coord.x + direction.x < 0 or coord.y + direction.y < 0 or coord.x + direction.x >= len(lines) or coord.y + direction.y >= len(lines[0]):
			continue
		
		# Check if at border of basin
		if int(data[coord.x + direction.x][coord.y + direction.y]) == 9:
			continue
		
		if visited[coord.x + direction.x][coord.y + direction.y] == False:
			visited[coord.x + direction.x][coord.y + direction.y] = True
			count += recursive_explore(data, visited, Coordinate(coord.x + direction.x, coord.y + direction.y))
	return count

sizes = list()
for low_point in low_points:
	sizes.append(recursive_explore(lines, visited, low_point) - 1)
	
sizes.sort()

top_elements = sizes[-3:]
solution2 = 1
for item in top_elements:
	solution2 *= item

print(solution2)