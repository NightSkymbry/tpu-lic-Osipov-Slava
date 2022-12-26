import csv
from collections import Counter as c

with open('9_task.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=';')
	a = 0
	for r in reader:
		r = list(map(int, r))
		n = list(c(r).most_common())
		first = n[0][1] == 2 and n[1][1] == 1
		second = sum(map(lambda x: x[0], n[1:]))/4 <= n[0][0] * 2
		if first and second:
			a += 1
	
print(a)
