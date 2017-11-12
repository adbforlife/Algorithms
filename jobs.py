import os

jobs = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'jobs.txt')) as file:
	jobs = file.readlines()
	jobs.pop(0)
	for i in range(len(jobs)):
		jobs[i] = jobs[i].rstrip()
		jobs[i] = jobs[i].split(" ")
		for j in range(len(jobs[i])):
			jobs[i][j] = int(jobs[i][j])
		jobs[i].append(jobs[i][0] - jobs[i][1])
		jobs[i].append(float(jobs[i][0]) / jobs[i][1])

jobsByDifference = sorted(jobs, key = lambda x : (-x[2], -x[1]))
time = 0
weightedTimes = 0
for i in jobsByDifference:
	time += i[1]
	weightedTimes += i[0] * time
print(weightedTimes)

jobsByRatio = sorted(jobs, key = lambda x : -x[3])
time2 = 0
weightedTimes2 = 0
for i in jobsByRatio:
	time2 += i[1]
	weightedTimes2 += i[0] * time2
print(weightedTimes2)