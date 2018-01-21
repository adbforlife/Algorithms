import os
import sys
items = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'tsp_large.txt')) as file:
	strings = file.readlines()
	strings.pop(0)
	for i in strings:
		items.append(map(float, i.rstrip().split(" ")))

def square_distance(index1, index2):
	return pow(items[index1 - 1][1] - items[index2 - 1][1], 2) + pow(items[index1 - 1][2] - items[index2 - 1][2], 2)

print(square_distance(2, 4))

path = [1]
remaining_locations = [i for i in range(2, 33709)]

while len(remaining_locations) > 0:
	if len(path) % 100 == 0:
		print(len(path))
	lowest_index = remaining_locations[0]
	lowest_distance = square_distance(remaining_locations[0], path[-1])
	for i in remaining_locations:
		if square_distance(i, path[-1]) < lowest_distance:
			lowest_distance = square_distance(i, path[-1])
			lowest_index = i
	path.append(lowest_index)
	remaining_locations.remove(lowest_index)


distance = 0
for i in range(0, len(path) - 1):
	distance += pow(square_distance(path[i], path[i + 1]), 0.5)
distance += pow(square_distance(path[0], path[-1]), 0.5)
print(distance)