from heapq import *
from heapq_max import *

inputs = []
medians = [6331, 2793]

with open("/Users/ADB/Desktop/ / /Python/Algorithms/medianMaintenance.txt") as file:
	strings = file.readlines()
	for i in strings:
		inputs.append(int(i.rstrip()))

bottomHeap = []
topHeap = []
heappush_max(bottomHeap, 2793)
heappush(topHeap, 6331)

for i in inputs[2:]:
	if i > topHeap[0]:
		heappush(topHeap, i)
		if len(topHeap) > len(bottomHeap):
			heappush_max(bottomHeap, heappop(topHeap))
		medians.append(bottomHeap[0])
	else:
		heappush_max(bottomHeap, i)
		if len(bottomHeap) - len(topHeap) > 1:
			heappush(topHeap, heappop_max(bottomHeap))
		medians.append(bottomHeap[0])

print(len(medians))
print(sum(medians))
print(sum(medians) % 10000)