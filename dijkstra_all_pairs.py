import os
import sys
from heapdict import *
from heapq import *

edges = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'large_graph.txt')) as file:
	strings = file.readlines()
	strings.pop(0)
	for i in strings:
		edges.append(map(int, i.rstrip().split(" ")))

graph = [[] for i in range(20000)]
for edge in edges:
	graph[edge[0] - 1].append(edge)

def dijkstra(num_vertices, graph, source):

	distances = [0 for i in range(num_vertices)]
	vertex_set = heapdict()

	for i in range(1, num_vertices + 1):
		if source != i:
			distances[i - 1] = float('inf')
		vertex_set[i] = distances[i - 1]

	while len(vertex_set) > 0:
		u = vertex_set.popitem()
		for neighbor_edge in graph[u[0] - 1]:
			alt = distances[u[0] - 1] + neighbor_edge[2]
			if alt < distances[neighbor_edge[1] - 1]:
				distances[neighbor_edge[1] - 1] = alt
				vertex_set[neighbor_edge[1]] = alt

	return distances
print("adb")
print(dijkstra(20000, graph, 1))