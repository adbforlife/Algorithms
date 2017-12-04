import os
import sys
numNodes = 0
weights = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'mwis.txt')) as file:
	strings = file.readlines()
	numNodes = int(strings[0].rstrip())
	strings.pop(0)
	for i in strings:
		weights.append(int(i.rstrip()))

solutions = [weights[0], max(weights[0], weights[1])]
for i in range(2, len(weights)):
	solutions.append(max(solutions[i - 1], solutions[i - 2] + weights[i]))

vertices = []
i = len(weights) - 1
while i >= 1:
	if solutions[i] == solutions[i - 1]:
		i -= 1
	else:
		vertices.append(i + 1)
		i -= 2
vertices.append(1)

for i in [1, 2, 3, 4, 17, 117, 517, 997]:
	if i in vertices:
		sys.stdout.write("1")
	else:
		sys.stdout.write("0")
sys.stdout.write("\n")