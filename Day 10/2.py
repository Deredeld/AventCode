
a = ["(",")"]
b = ["[","]"]
c = ["{","}"]
d = ["<",">"]
points = {")":1,"]":2,"}":3,">":4}
lis = a+b+c+d

def parseLine(input):
	score=0
	pipe = []
	for s in input:
		if s == a[0]:
			pipe.append(s)
		elif s == a[1] and pipe[-1] == a[0]:
			del pipe[-1]
		elif s == b[0]:
			pipe.append(s)
		elif s == b[1] and pipe[-1] == b[0]:
			del pipe[-1]
		elif s == c[0]:
			pipe.append(s)
		elif s == c[1] and pipe[-1] == c[0]:
			del pipe[-1]
		elif s == d[0]:
			pipe.append(s)
		elif s == d[1] and pipe[-1] == d[0]:
			del pipe[-1]
		else:
			return 0

	for v in reversed(pipe):
		if pipe[-1]==a[0]:
			score=score*5+points[a[1]]
			del pipe[-1]
		elif pipe[-1]==b[0]:
			score=score*5+points[b[1]]
			del pipe[-1]
		elif pipe[-1]==c[0]:
			score=score*5+points[c[1]]
			del pipe[-1]
		elif pipe[-1]==d[0]:
			score=score*5+points[d[1]]
			del pipe[-1]
	return score

with open("input.txt", "r") as f:
	total = []
	for line in f.read().splitlines():
		score = parseLine(line)
		if score !=0:
			total.append(score)
	total = sorted(total)
	print(total[int(len(total)/2)])