import os
from heapq import *
numAlphabet = 0
weights = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'huffman.txt')) as file:
	strings = file.readlines()
	numAlphabet = int(strings[0].rstrip())
	strings.pop(0)
	for i in strings:
		weights.append(int(i.rstrip()))
weights.sort()

weights2 = []
for i in weights:
	weights2.append(i)

heapify(weights)
heap = weights
length = 0
currentNode = heap[0]
while len(heap) > 1:
	weight1 = heappop(heap)
	weight2 = heappop(heap)
	if (currentNode == weight1 or currentNode == weight2):
		heappush(heap, weight1 + weight2)
		currentNode = weight1 + weight2
		length += 1
	else:
		heappush(heap, weight1 + weight2)
print(length)

heapify(weights2)
heap = weights2
length = 0
currentNode = max(heap)
while len(heap) > 1:
	weight1 = heappop(heap)
	weight2 = heappop(heap)
	if (currentNode == weight1 or currentNode == weight2):
		heappush(heap, weight1 + weight2)
		currentNode = weight1 + weight2
		length += 1
	else:
		heappush(heap, weight1 + weight2)
print(length)