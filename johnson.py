import os
import sys
from heapdict import *
from heapq import *

edges1 = []
edges2 = []
edges3 = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'g1.txt')) as file:
	strings = file.readlines()
	strings.pop(0)
	for i in strings:
		edges1.append(map(int, i.rstrip().split(" ")))
with open(os.path.join(__location__, 'g2.txt')) as file:
	strings = file.readlines()
	strings.pop(0)
	for i in strings:
		edges2.append(map(int, i.rstrip().split(" ")))
with open(os.path.join(__location__, 'g3.txt')) as file:
	strings = file.readlines()
	strings.pop(0)
	for i in strings:
		edges3.append(map(int, i.rstrip().split(" ")))

def bellman_ford(num_vertices, edges):
	distances = [0 for i in range(num_vertices + 1)]
	predecessors = [0 for i in range(num_vertices + 1)]

	for i in range(num_vertices):
		distances[i + 1] = float('inf')
		predecessors[i + 1] = -1

	distances[0] = 0
	predecessors[0] = -1

	for i in range(1, num_vertices):
		for edge in edges:
			if distances[edge[0]] + edge[2] < distances[edge[1]]:
				distances[edge[1]] = distances[edge[0]] + edge[2]
				predecessors[edge[1]] = edge[0]

	for edge in edges:
		if distances[edge[0]] + edge[2] < distances[edge[1]]:
			raise NameError('Graph contains negative cycle')

	return distances

def dijkstra(num_vertices, edges, source):
	graph = [[] for i in range(num_vertices)]
	for edge in edges:
		graph[edge[0] - 1].append(edge)

	distances = [0 for i in range(num_vertices)]
	vertex_set = heapdict()

	for i in range(1, num_vertices + 1):
		if source != i:
			distances[i - 1] = float('inf')
		vertex_set[i] = distances[i - 1]
		#heappush(vertex_set, (distances[i - 1], i))

	while len(vertex_set) > 0:
		u = vertex_set.popitem()
		for neighbor_edge in graph[u[0] - 1]:
			alt = distances[u[0] - 1] + neighbor_edge[2]
			#print(alt)
			if alt < distances[neighbor_edge[1] - 1]:
				distances[neighbor_edge[1] - 1] = alt
				vertex_set[neighbor_edge[1]] = alt

	return distances


dummy_edges = [[0, i, 0] for i in range(1, 1001)]

edges1 = dummy_edges + edges1
edges2 = dummy_edges + edges2
edges3 = dummy_edges + edges3

d = bellman_ford(1000, edges3)
edges3 = edges3[1000:]
for edge in edges3:
	edge[2] = edge[2] + d[edge[0]] - d[edge[1]]

print(len(d))
shortest_paths = []
for i in range(1, 1001):
	for j in range(1, 1001):
		shortest_paths.append(d[i] - d[j])
shortest_paths.sort()
print(shortest_paths[-1])
dijkstra(1000, edges3, 1)