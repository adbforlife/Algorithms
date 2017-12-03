import os

class UnionFindChild:
	def __init__ (self, number):
		self.number = number
		self.parent = self
		self.rank = 0

def find(x):
	if x.parent.number != x.number:
		x.parent = find(x.parent)
	return x.parent

def union(x, y):
	xRoot = find(x)
	yRoot = find(y)
	if xRoot.number == yRoot.number:
		return
	if xRoot.rank < yRoot.rank:
		xRoot.parent = yRoot
	elif xRoot.rank > yRoot.rank:
		yRoot.parent = xRoot
	else:
		yRoot.parent = xRoot
		xRoot.rank += 1

unionFindNodes = [UnionFindChild(i) for i in range(1, 501)]
unionFind = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'unionFind.txt')) as file:
	strings = file.readlines()
	strings.pop(0)
	for i in strings:
		array = i.rstrip().split(" ")
		for j in range(len(array)):
			array[j] = int(array[j])
		unionFind.append(array)

unionFind = sorted(unionFind, key=lambda x : x[2])
numClusters = 500
for i in unionFind:
	node1 = unionFindNodes[i[0] - 1]
	node2 = unionFindNodes[i[1] - 1]
	weight = i[2]
	if numClusters != 4:
		if find(node1) != find(node2):
			union(node1, node2)
			numClusters -= 1
	else:
		if find(node1) != find(node2):
			print(weight)
			break