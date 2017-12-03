import os

numbers = []
numClusters = 0
numBits = 0
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'clusteringBig.txt')) as file:
	numbers = file.readlines()
	firstLine = numbers[0].rstrip().split(" ")
	numClusters = int(firstLine[0])
	numBits = int(firstLine[1])
	numbers.pop(0)
	for i in range(len(numbers)):
		numbers[i] = int(numbers[i].rstrip().replace(" ", ""), 2)
	numbers.sort()
	for i in range(len(numbers)):
		numbers[i] = [numbers[i], 0, i]

numClusters2 = numClusters

def find(index):
	if numbers[index][2] != index:
		numbers[index][2] = find(numbers[index][2])
	return numbers[index][2]
def union(index1, index2):
	rootIndex1 = find(index1)
	rootIndex2 = find(index2)
	if rootIndex1 == rootIndex2:
		return
	else:
		numbers[rootIndex1][2] = rootIndex2
		global numClusters
		numClusters -= 1

xors1 = []
for i in range(numBits):
	xors1.append(pow(2, i))

xors2 = []
for i in range(numBits - 1):
	for j in range(i + 1, numBits):
		xors2.append(pow(2, i) + pow(2, j))

def findPossibleDistance1(index):
	results = []
	for i in xors1:
		results.append(numbers[index][0] ^ i)
	return results
def findPossibleDistance2(index):
	results = []
	for i in xors2:
		results.append(numbers[index][0] ^ i)
	return results

def findIndex(number):
	hiIndex = numClusters2 - 1
	loIndex = 0
	midIndex = (hiIndex + loIndex) // 2
	while (hiIndex >= loIndex):
		if number > numbers[midIndex][0]:
			loIndex = midIndex + 1
		elif number < numbers[midIndex][0]:
			hiIndex = midIndex - 1
		else:
			return midIndex
		midIndex = (hiIndex + loIndex) // 2
	return -1

for i in range(len(numbers) - 1):
	if numbers[i][0] == numbers[i + 1][0]:
		union(i, i + 1)
print(numClusters)
for i in range(len(numbers)):
	possibles = findPossibleDistance1(i)
	for j in possibles:
		possibleIndex = findIndex(j)
		if possibleIndex != -1:
			union(possibleIndex, i)
print(numClusters)

for i in range(len(numbers)):
	if i % (numClusters2 // 100) == 0:
		print(str(100.0 * i / numClusters2) + "%")
	possibles = findPossibleDistance2(i)
	for j in possibles:
		possibleIndex = findIndex(j)
		if possibleIndex != -1:
			union(possibleIndex, i)
print(numClusters)