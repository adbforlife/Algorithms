import random
import sys

testCase = [
	[1, 2],
	[1, 5],
	[2, 3],
	[2, 6],
	[3, 7],
	[4, 1],
	[4, 8],
	[5, 4],
	[5, 2],
	[5, 9],
	[6, 3],
	[7, 6],
	[8, 11],
	[9, 6],
	[9, 8],
	[9, 10],
	[10, 6],
	[10, 8],
	[11, 9],
	[11, 10]
]

class SCC:
	def __init__ (self, numbers, n):
		self.n = n
		self.numbers = numbers
		self.adjacencyList = [[i] for i in range(1, n + 1)]
		for i in numbers:
			self.adjacencyList[i[0] - 1].append(i[1])
		self.reversedAdjacencyList = [[i] for i in range(1, n + 1)]
		for i in numbers:
			self.reversedAdjacencyList[i[1] - 1].append(i[0])

		self.finishingList = []
		self.explorationList = [[i, 0] for i in range(1, n + 1)]
		self.secondExplorationList = [[i, 0] for i in range(1, n + 1)]

		self.SCCSizes = []

	def reverseExplore(self, i):
		waitStack = []
		waitStack.append(i)
		while (len(waitStack) > 0):
			j = waitStack.pop()
			if (self.explorationList[j - 1][1] == 0):
				self.finishingList.insert(0, j)
				self.explorationList[j - 1][1] = 1
				for k in self.reversedAdjacencyList[j - 1][1:]:
					waitStack.append(k)
		print(str(round(100.0 * len(self.finishingList) / self.n, 2)) + "%")

	def explore(self, i):
		scc = []
		waitStack = []
		waitStack.append(i)
		while (len(waitStack) > 0):
			j = waitStack.pop()
			if (self.secondExplorationList[j - 1][1] == 0):
				scc.append(j)
				self.secondExplorationList[j - 1][1] = 1
				for k in self.adjacencyList[j - 1][1:]:
					waitStack.append(k)
		self.SCCSizes.append(len(scc))
		print(str(round(100.0 * sum(self.SCCSizes) / self.n, 2)) + "%")

	def fullReverseExplore(self):
		for i in range(1, self.n + 1):
			if self.explorationList[i - 1][1] == 0:
				self.reverseExplore(i)

	def fullExplore(self):
		for i in self.finishingList:
			if self.secondExplorationList[i - 1][1] == 0:
				self.explore(i)



sys.setrecursionlimit(1500)
graph = SCC(testCase, 11)
graph.fullReverseExplore()
print(graph.finishingList)
graph.fullExplore()
print(sorted(graph.SCCSizes))


file = open("/Users/ADB/Desktop/ / /Python/Algorithms/strongConnectedComponents.txt", "r")
strings = file.readlines()
file.close()
webGraph = []
for i in strings:
	temp = i.rstrip().split(" ")
	webGraph.append([int(temp[0]), int(temp[1])])

print(webGraph[0])
web = SCC(webGraph, 875714)
web.fullReverseExplore()
print(web.finishingList[0])
web.fullExplore()
print(sorted(web.SCCSizes))
