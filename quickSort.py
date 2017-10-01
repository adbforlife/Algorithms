import copy
file = open("/Users/ADB/Desktop/ / /Python/Algorithms/quickSort.txt", "r")
strings = file.readlines()
file.close()
evilArray = []
for string in strings:
	evilArray.append(int(string.rstrip()))

comparisons = 0
comparisons2 = 0

class QS:
	def __init__ (self):
		self.comparisons = 0

	def quickSort(self, numbers):
		self.comparisons += len(numbers) - 1
		if (len(numbers) == 1):
			return numbers
		else:
			pivot = numbers[0]
			j = 0
			for i in range(1, len(numbers)):
				if numbers[i] < pivot:
					j += 1
					numbers[j], numbers[i] = numbers[i], numbers[j]
			numbers[j], numbers[0] = numbers[0], numbers[j]
			return (self.quickSort(numbers[0:j]) if j > 0 else []) + [pivot] + (self.quickSort(numbers[j + 1:len(numbers)]) if j < len(numbers) - 1 else [])

	def quickSort2(self, numbers):
		self.comparisons += len(numbers) - 1
		if (len(numbers) == 1):
			return numbers
		else:
			numbers[0], numbers[len(numbers) - 1] = numbers[len(numbers) - 1], numbers[0]
			pivot = numbers[0]
			j = 0
			for i in range(1, len(numbers)):
				if numbers[i] < pivot:
					j += 1
					numbers[j], numbers[i] = numbers[i], numbers[j]
			numbers[j], numbers[0] = numbers[0], numbers[j]
			return (self.quickSort2(numbers[0:j]) if j > 0 else []) + [pivot] + (self.quickSort2(numbers[j + 1:len(numbers)]) if j < len(numbers) - 1 else [])

	def quickSort3(self, numbers):
		self.comparisons += len(numbers) - 1
		if (len(numbers) == 1):
			return numbers
		else:
			pivots = [numbers[0], numbers[(len(numbers) + 1) // 2 - 1], numbers[len(numbers) - 1]]
			pivot = sorted(pivots)[1]
			pivotPos = 0
			if numbers[len(numbers) - 1] == pivot:
				pivotPos = len(numbers) - 1
			elif numbers[(len(numbers) + 1) // 2 - 1] == pivot:
				pivotPos = (len(numbers) + 1) // 2 - 1
			numbers[0], numbers[pivotPos] = numbers[pivotPos], numbers[0]

			#pivot = numbers[0]
			j = 0
			for i in range(1, len(numbers)):
				if numbers[i] < pivot:
					j += 1
					numbers[j], numbers[i] = numbers[i], numbers[j]
			numbers[j], numbers[0] = numbers[0], numbers[j]
			return (self.quickSort3(numbers[0:j]) if j > 0 else []) + [pivot] + (self.quickSort3(numbers[j + 1:len(numbers)]) if j < len(numbers) - 1 else [])


comp1 = QS()
comp1.quickSort(copy.copy(evilArray))
print(comp1.comparisons)

comp2 = QS()
comp2.quickSort2(copy.copy(evilArray))
print(comp2.comparisons)

comp3 = QS()
comp3.quickSort3(copy.copy(evilArray))
print(comp3.comparisons)

comp4 = QS()
print(comp4.quickSort3([3, 8, 2, 5, 1, 4, 7, 6]))