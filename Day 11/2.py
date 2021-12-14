
class cells():
	def __init__(self):
		self.alreadyGlowed = []
		self.numberofGlows = 0

	def increase(self,matrix,y,x):
		if matrix[y][x]<9 and [y,x] not in self.alreadyGlowed:
			matrix[y][x]+=1
		elif [y,x] not in self.alreadyGlowed:
			self.numberofGlows+=1
			matrix[y][x]=0
			self.alreadyGlowed.append([y,x])
			if x!=0:
 				self.increase(matrix,y,x-1)
			if x!=9:
				self.increase(matrix,y,x+1)
			if y!=0:
				self.increase(matrix,y-1,x)
			if y!=9:
				self.increase(matrix,y+1,x)
			if x!=0 and y!=0:
				self.increase(matrix,y-1,x-1)
			if x!=9 and y!=0:
				self.increase(matrix,y-1,x+1)
			if x!=0 and y!=9:
				self.increase(matrix,y+1,x-1)
			if x!=9 and y!=9:
				self.increase(matrix,y+1,x+1)

	def newRound(self):
		self.alreadyGlowed = []


def printMat(mat):
	for line in mat:
		print(line)
	print("---------------")


with open("input.txt", "r") as f:
	matrix = []
	for line in f.read().splitlines():
		matrix.append([int(a) for a in line])

	nb = 0
	cel  = cells()
	for i in range(346):
		for y in range(10):
			for x in range(10):
				cel.increase(matrix,y,x)
		cel.newRound()
		printMat(matrix)
	print("346")

