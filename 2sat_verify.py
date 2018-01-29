import os
import sys
from random import *

scc = []

with open("/Users/ADB/Desktop/example.txt") as file:
	strings = file.readlines()
	total_length = int(strings.pop(0))
	for i in strings:
		scc.append(map(int, i.rstrip().split(" ")))

biggest = 0

for i in scc:
    if len(i) > biggest:
        biggest = len(i)
    if len(i) > 1:
        for j in i:
            for k in i:
                if j + k == 0:
                    print("fail")
print("pass")
print(biggest)
