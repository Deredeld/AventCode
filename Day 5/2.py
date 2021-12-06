import re

class vector:
	def __init__(self, line):
		print(line)
		result = re.search(r"(\d*),(\d*) -> (\d*),(\d*)",line)
		self.x1 = int(result.group(1))
		self.y1 = int(result.group(2))
		self.x2 = int(result.group(3))
		self.y2 = int(result.group(4))
	def __str__(self):
		return str(self.x1) + "," + str(self.y1) + " -> "  + str(self.x2) + "," + str(self.y2) 
#Get first line
with open("input.txt", "r") as f:

	content = f.readlines()
	VectorList = []
	for line in content:
		VectorList.append(vector(line))

	print("-----")
	for vector in VectorList:
		print(vector)

	map = [[0 for col in range(1000)] for row in range(1000)]


	print("-----")
	for vector in VectorList:
		if vector.x1 == vector.x2:
			for i in range(min(vector.y1,vector.y2),max(vector.y1,vector.y2)+1):
				map[i][vector.x1]+=1
		elif vector.y1 == vector.y2:
			for i in range(min(vector.x1,vector.x2),max(vector.x1,vector.x2)+1):
				map[vector.y1][i]+=1
		#If diag
		elif vector.x1+vector.x2 == vector.y1+vector.y2 or abs(vector.x1-vector.x2) == abs(vector.y1-vector.y2):
			print("diag")
			print(vector)
			#Case down top
			if vector.x1<vector.x2 and vector.y1<vector.y2:
				print("Case 1")
				x3 = vector.x1
				y3 = vector.y1
				while y3 != vector.y2:
					map[y3][x3]+=1
					y3+=1
					x3+=1
				map[y3][x3]+=1

			elif vector.x1>vector.x2 and vector.y1>vector.y2:
				print("Case 2")
				x3 = vector.x1
				y3 = vector.y1
				while y3 != vector.y2:
					print(x3,y3)
					map[y3][x3]+=1
					y3-=1
					x3-=1
				map[y3][x3]+=1

			elif vector.x1<vector.x2 and vector.y1>vector.y2:
				print("Case 3")
				x3 = vector.x1
				y3 = vector.y1
				while y3 != vector.y2:
					map[y3][x3]+=1
					y3-=1
					x3+=1
				map[y3][x3]+=1

			elif vector.x1>vector.x2 and vector.y1<vector.y2:
				print("Case 4")
				x3 = vector.x1
				y3 = vector.y1
				while y3 != vector.y2:
					map[y3][x3]+=1
					y3+=1
					x3-=1
				map[y3][x3]+=1

	#count overlaps
	overlaps = 0
	for row in map:
		print(row)
		for number in row:
			if number >1:
				overlaps+=1
	print(overlaps)