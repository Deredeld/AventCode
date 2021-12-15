import re
from collections import Counter

def step(polymer,trans):
	base = [polymer[0]]
	for i in range(len(polymer)-1):
		inserted = False
		for t in trans:
			if not inserted:
				if polymer[i]+polymer[i+1] == t[0]:
					base.append(t[1])
					base.append(polymer[i+1])
					inserted = True
		if not inserted:
			base.append(polymer[i])
	return base

def split(word):
    return [char for char in word[0:-1]]

with open("input.txt", "r") as f:
	base = f.readline()

	listMarks = []

	for line in f.read().splitlines():
		nodes = re.search(r"([A-Z]*?) -> ([A-Z])",line)
		if nodes:
			listMarks.append([nodes.group(1),nodes.group(2)])
	base = split(base)
	new= []
	for i in range(10):
		base = step(base,listMarks)
	m = Counter(base)
	print(m)
	print(m[max(m, key=m.get)]-m[min(m, key=m.get)])