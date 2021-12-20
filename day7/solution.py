from scipy.optimize import minimize

with open("input.txt") as file:
	lines = file.read().strip().split(',')

crabs = [int(x) for x in lines]

def calc_fuel(final_pos, x):
	sum = 0
	for item in x:
		sum += abs(item - final_pos)
	return sum

final_pos = 4

result = minimize(calc_fuel, final_pos, args=(crabs.copy()), method = 'Nelder-Mead')

print(result.fun)

def get_dist(start, end):
	distance = abs(start - end)
	result = 0
	while distance > 0:
		result+= distance
		distance -= 1
	return result

def calc_fuel2(final_pos, x):
	sum = 0
	for item in x:
		sum += get_dist(item, final_pos)
	return sum

final_pos = 2

result2 = minimize(calc_fuel2, final_pos, args=(crabs.copy()), method = 'Nelder-Mead')

print(result2.fun)