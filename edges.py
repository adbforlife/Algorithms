import os

graph = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'edges.txt')) as file:
	graph = file.readlines()
	graph.pop(0)
	for i in range(len(graph)):
		graph[i] = graph[i].rstrip()
		graph[i] = graph[i].split(" ")
		for j in range(len(graph[i])):
			graph[i][j] = int(graph[i][j])

mstCost = 0
mstVertices = [1]
while (len(mstVertices) != 500):
	minIndex = 0
	minCost = 100000
	for i in range(len(graph)):
		if ((graph[i][0] in mstVertices) and (not graph[i][1] in mstVertices)) or ((graph[i][1] in mstVertices) and (not graph[i][0] in mstVertices)):
			if graph[i][2] < minCost:
				minIndex = i
				minCost = graph[i][2]
	if graph[minIndex][0] in mstVertices:
		mstVertices.append(graph[minIndex][1])
		mstCost += minCost
	else:
		mstVertices.append(graph[minIndex][0])
		mstCost += minCost
print(mstCost)