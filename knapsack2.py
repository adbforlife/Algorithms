import os
import sys
items = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'knapsack2.txt')) as file:
	strings = file.readlines()
	strings.pop(0)
	for i in strings:
		items.append(map(int, i.rstrip().split(" ")))

cache = {}

for x in range(0, 2000001):
	cache[(0, x)] = 0

sys.setrecursionlimit(10000)

def answer(numItem, maxWeight):
	if (numItem, maxWeight) in cache:
		return cache[(numItem, maxWeight)]
	else:
		value = items[numItem - 1][0]
		weight = items[numItem - 1][1]
		prev1 = answer(numItem - 1, maxWeight)
		if weight > maxWeight:
			cache[(numItem, maxWeight)] = prev1
			return prev1
		else:
			prev2 = answer(numItem - 1, maxWeight - weight)
			cache[(numItem, maxWeight)] = max(prev1, prev2 + value)
			return max(prev1, prev2 + value)

print(answer(2000,2000000))