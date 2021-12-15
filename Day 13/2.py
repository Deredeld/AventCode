import re



def foldY(mat,pos):
	for i in range(pos[1]+1,len(mat)):
		for m in range(len(mat[i])):
			if mat[i][m]=="#":
				mat[i][m]="."
				mat[pos[1]-(i-pos[1])][m]="#"

def foldX(mat,pos):
	for i in range(len(mat)):
		for m in range(pos[1]+1,len(mat[i])):
			if mat[i][m]=="#":
				mat[i][m]="."
				mat[i][pos[1]-(m-pos[1])]="#"



with open("input.txt", "r") as f:
	listMarks = []
	listFolds = []
	for line in f.read().splitlines():
		nodes = re.search(r"(\d*),(\d*)",line)
		if nodes:
			listMarks.append([int(nodes.group(1)),int(nodes.group(2))])
		foldsY = re.search(r"y=(\d*)",line)
		if foldsY:
			listFolds.append(["y",int(foldsY.group(1))])
		foldsX = re.search(r"x=(\d*)",line)
		if foldsX:
			listFolds.append(["x",int(foldsX.group(1))])

	print(listMarks)
	print(listFolds)
	maxX = 0
	maxY = 0
	for marks in listMarks:
		if marks[0]> maxX:
			maxX = marks[0]
		if marks[1]> maxY:
			maxY = marks[1]
	print(maxY,maxX)


	mat = [["." for x in range(maxX+1)] for y in range(maxY+1)]

	for value in listMarks:
		mat[value[1]][value[0]] = "#"

	print(listFolds)
	for folds in listFolds:
		if folds[0]=="y":
			foldY(mat,folds)
		else:
			foldX(mat,folds)

	c = 0
	for line in mat:
		for i in line:
			if i == "#":
				c+=1

	for line in mat:
		print("".join(line))

	print(c)