scores = [0]
explored = [1]
unexplored = [i for i in range(2, 201)]

file = open("/Users/ADB/Desktop/ / /Python/Algorithms/dijkstraData.txt", "r")
strings = file.readlines()
file.close()

graph = []
for string in strings:
	graph.append(string.rstrip().split("\t")[1:])

for i in graph:
	for j in range(0, len(i)):
		temp = i[j].split(",")
		temp[0] = int(temp[0])
		temp[1] = int(temp[1])
		i[j] = temp

while(len(explored) != 200):
	tempscores = [1000000 for i in range(200)]
	for i in explored:
		for j in range(0, len(graph[i - 1])):
			endPoint = graph[i - 1][j][0]
			distance = graph[i - 1][j][1] + scores[explored.index(i)]
			if not endPoint in explored:
				tempscores[endPoint - 1] = min(tempscores[endPoint - 1], distance)
	nextPoint = tempscores.index(min(tempscores)) + 1
	nextScore = tempscores[nextPoint - 1]
	explored.append(nextPoint)
	scores.append(nextScore)

testArray = [7,37,59,82,99,115,133,165,188,197]
results = []
for i in testArray:
	results.append(scores[explored.index(i)])
print(results)