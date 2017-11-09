import os

numbers = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, '2Sum.txt')) as file:
	for i in file.readlines():
		numbers.append(int(i.rstrip()))

hashTable = {}
for i in numbers:
	if not i in hashTable:
		hashTable[i] = 1

print("done with processing")


count = 0
for t in range(-10000, 10001):
	for i in numbers:
		target = t - i
		if target in hashTable:
			count += 1
			print(count)
			print(t)
			break

print(count)