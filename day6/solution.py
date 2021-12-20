from collections import defaultdict


with open("input.txt") as file:
	lines = file.read().splitlines()

fish = [int(x) for x in lines[0].split(',')]


days = 80
it = 0
while it < days:
	add_fish_ctr = 0
	for i in range(len(fish)):
		if fish[i] == 0:
			add_fish_ctr += 1
			fish[i] = 6
		else:
			fish[i] -= 1

	for j in range(add_fish_ctr):
		fish.append(8)
	it += 1 

print(len(fish))

fish = [int(x) for x in lines[0].split(',')]

lookup = defaultdict(int)
for f in fish:
	if f not in lookup:
		lookup[f] = 0
	lookup[f] += 1

it = 0
days = 256
while it < days:
	add_fish_ctr = 0
	newLookup = defaultdict(int)
	for key, nr in lookup.items():
		if key == 0:
			newLookup[6] += nr
			newLookup[8] += nr
		else:
			newLookup[key - 1] += nr
	lookup = newLookup

	it += 1 

print(sum(lookup.values()))