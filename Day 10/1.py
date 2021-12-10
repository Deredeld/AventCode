
a = ["(",")"]
b = ["[","]"]
c = ["{","}"]
d = ["<",">"]
points = {")":3,"]":57,"}":1197,">":25137}
lis = a+b+c+d

def parseLine(input):
	pipe = [""]
	for s in input:
		print(input.index(s))
		print(s)
		if s == a[0]:
			pipe.append(s)
		elif s == a[1] and pipe[-1] == a[0]:
			print("del a")
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
			print("Error")
			print(s)
			print(pipe)
			return points[s]
	return 0

with open("input.txt", "r") as f:
	total = 0
	for line in f.read().splitlines():
		total += parseLine(line)
	print(total)