file = open("/Users/ADB/Desktop/ / /Python/Algorithms/inversions.txt", "r")
strings = file.readlines()
file.close()
evilArray = []
for string in strings:
	evilArray.append(int(string.rstrip()))

def mergeSort(numbers):
	if (len(numbers) == 1):
		return numbers
	elif (len(numbers) == 2):
		if (numbers[0] < numbers[1]):
			return numbers
		else:
			return numbers[::-1]
	else:
		firstHalf = mergeSort(numbers[0:len(numbers)//2])
		secondHalf = mergeSort(numbers[len(numbers)//2:len(numbers)])
		final = []
		i = 0
		j = 0
		for k in range(len(numbers)):
			if j == len(secondHalf) or (i != len(firstHalf) and firstHalf[i] < secondHalf[j]):
				final.append(firstHalf[i])
				i += 1
			else:
				final.append(secondHalf[j])
				j += 1
		return final

def countInversions(numbers):
	if (len(numbers) == 1):
		return 0
	elif (len(numbers) == 2):
		if numbers[0] < numbers[1]:
			return 0
		else:
			return 1
	else:
		normalInversions = countInversions(numbers[0:len(numbers)//2]) + countInversions(numbers[len(numbers)//2:len(numbers)])
		firstHalf = sorted(numbers[0:len(numbers)//2])
		secondHalf = sorted(numbers[len(numbers)//2:len(numbers)])
		splitInversions = 0
		i = 0
		j = 0
		for k in range(len(numbers)):
			if j == len(secondHalf) or (i != len(firstHalf) and firstHalf[i] < secondHalf[j]):
				i += 1
			else:
				j += 1
				splitInversions += len(firstHalf) - i
		return normalInversions + splitInversions

print(countInversions(evilArray))