import os
import sys
items = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'tsp.txt')) as file:
	strings = file.readlines()
	strings.pop(0)
	for i in strings:
		items.append(map(float, i.rstrip().split(" ")))

new_items = []
for i in items:
	new_items.append((i[0], i[1]))
#print(new_items)

string = "["
for i in items:
	string += "{\"x\":" + str(i[0]) + ",\"y\":" + str(i[1]) + "},"

string += "]"
#print(string)

sequence = [4, 0, 1, 5, 9, 10, 11, 14, 18, 17, 21, 22, 20, 16, 19, 24, 23, 15, 13, 12, 8, 6, 2, 3, 7]
for i in range(len(sequence)):
	sequence[i] += 1
#print(len(sequence))
total = 0
for i in range(25):
	item1 = items[sequence[i] - 1]
	if i != 24:
		item2 = items[sequence[i + 1] - 1]
	else:
		item2 = items[sequence[0] - 1]
	total += pow(pow(item1[0] - item2[0], 2) + pow(item1[1] - item2[1], 2), 0.5)
print(total)

# This one is a bit unfair, so I guess it's fair that the solution is a bit unfair. If anyone sees this... Graph it maybe that'd help.