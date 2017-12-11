import os
import sys
items = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'knapsack1.txt')) as file:
	strings = file.readlines()
	strings.pop(0)
	for i in strings:
		items.append(map(int, i.rstrip().split(" ")))

answers = [[0 for i in range(10001)] for j in range(101)]
for i in range(1, 101):
	for x in range(10001):
		value = items[i - 1][0]
		weight = items[i - 1][1]
		if weight > x:
			answers[i][x] = answers[i - 1][x]
		else:
			answers[i][x] = max(answers[i - 1][x], answers[i - 1][x - weight] + value)

print(answers[100][10000])