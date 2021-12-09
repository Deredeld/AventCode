

def getNeighbor(listValues,matrix,x,y):
	if  x<0 or y<0 or x>=len(matrix[0]) or y>=len(matrix) or matrix[y][x]==9 :
		return listValues
	else:
		listValues.append([y,x])
		if [y-1,x] not in listValues:
			getNeighbor(listValues,matrix,x,y-1)
		if [y+1,x] not in listValues:
			getNeighbor(listValues,matrix,x,y+1)

		if [y,x-1] not in listValues:
			getNeighbor(listValues,matrix,x-1,y)
		if [y,x+1] not in listValues:
			getNeighbor(listValues,matrix,x+1,y)
	return listValues




with open("input.txt", "r") as f:
	matrix = []
	for line in f.read().splitlines():
			row = []
			for number in line:
				row.append(int(number))
			matrix.append(row)

	listBassins = []
	for y in range(len(matrix)):
		for x in range(len(matrix[0])):
			size = sorted(getNeighbor([],matrix,x,y))
			if size not in listBassins:
				listBassins.append(size)
	
	sizes =[]
	for liste in listBassins:
		sizes.append(len(liste))

	final = 1
	for size in sorted(sizes, reverse=True)[:3]:
		final = final * size
	print(final)