import random

originalTestCase = [
	[1, 2, 5, 6],
	[2, 1, 5, 6, 3],
	[3, 2, 7, 8, 4],
	[4, 3, 7, 8],
	[5, 1, 2, 6],
	[6, 5, 1, 2, 7],
	[7, 6, 3, 4, 8],
	[8, 7, 3, 4]
]

file = open("/Users/ADB/Desktop/ / /Python/Algorithms/minCutGraph.txt", "r")
strings = file.readlines()
file.close()
originalTestCase = []
for i in strings:
	tempList = i.split('\t')
	tempList.pop(len(tempList) - 1)
	for j in range(0, len(tempList)):
		tempList[j] = int(tempList[j])
	originalTestCase.append(tempList)

print(originalTestCase)

def transformList(numbers):
	newList = []
	for i in numbers:
		for j in range(1, len(i)):
			newList.append([i[0], i[j]])
	return newList

def kargerMinCut(n, numbers):
	if (n == 2):
		return len(numbers) // 2
	else:
		mergePair = numbers[random.randrange(0, len(numbers))]
		mergeFromNum = mergePair[0]
		mergeToNum = mergePair[1]

		removeList = []
		for i in range(0, len(numbers)):
			if numbers[i][0] == mergeFromNum:
				if numbers[i][1] == mergeToNum:
					removeList.append(i)
				else:
					numbers[i][0] = mergeToNum
			if numbers[i][1] == mergeFromNum:
				if numbers[i][0] == mergeToNum:
					removeList.append(i)
				else:
					numbers[i][1] = mergeToNum
		for i in sorted(removeList, reverse = True):
			numbers.pop(i)

		return kargerMinCut(n - 1, numbers)

for i in range(40000):
	print(kargerMinCut(200, transformList(originalTestCase)))