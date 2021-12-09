with open("input.txt", "r") as f:
	matrix = []
	for line in f.read().splitlines():
			row = []
			for number in line:
				row.append(number)
			matrix.append(row)
	width = len(matrix[0])-1
	height = len(matrix)-1
	lowPoints=[]
	#Corners
	if matrix[0][0]<matrix[0][1] and matrix[0][0]<matrix[1][0]:
		lowPoints.append(int(matrix[0][0]))
		print("top left")
	if matrix[0][width]<matrix[0][width-1] and matrix[0][width]<matrix[1][width]:
		lowPoints.append(int(matrix[0][width]))
		print("top right")
	if matrix[height][0]<matrix[height][1] and matrix[height][0]<matrix[height-1][0]:
		lowPoints.append(int(matrix[height][0]))
		print("bottom left")
	if matrix[height][width]<matrix[height][width-1] and matrix[height][width]<matrix[height-1][width]:
		lowPoints.append(int(matrix[height][width]))
		print("bottom right")

	#Top
	for j in range(1,width):
		if(matrix[0][j]<matrix[0][j-1] and matrix[0][j]<matrix[0][j+1] and matrix[0][j]<matrix[1][j]):
			print("Top",matrix[0][j])
			lowPoints.append(int(matrix[0][j]))
	#Bottom
	for j in range(1,width):
		if(matrix[height][j]<matrix[height][j-1] and matrix[height][j]<matrix[height][j+1] and matrix[height][j]<matrix[height-1][j]):
			print("Bottom",matrix[height][j])
			lowPoints.append(int(matrix[height][j]))
	#Left
	for j in range(1,height):
		if(matrix[j][0]<matrix[j-1][0] and matrix[j][0]<matrix[j+1][0] and matrix[j][0]<matrix[j][1]):
			print("Left",matrix[j][0])
			lowPoints.append(int(matrix[j][0]))
	#Right
	for j in range(1,height):
		if(matrix[j][width]<matrix[j-1][width] and matrix[j][width]<matrix[j+1][width] and matrix[j][width]<matrix[j][width-1]):
			print("Right",matrix[j][width])
			lowPoints.append(int(matrix[j][width]))

	#Rest
	for j in range(1,height):
		for i in range(1,width):
			if matrix[j][i]<matrix[j][i+1] and matrix[j][i]<matrix[j][i-1] and matrix[j][i]<matrix[j+1][i] and matrix[j][i]<matrix[j-1][i]:
				print(matrix[j][i])
				lowPoints.append(int(matrix[j][i]))

	print(sum(lowPoints)+len(lowPoints))