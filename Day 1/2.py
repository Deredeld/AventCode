with open("input.txt", "r") as f:
	temp = f.read().splitlines()
	j = 0
	for i in range(3,len(temp)):
		if int(temp[i-3])+int(temp[i-2])+int(temp[i-1]) < int(temp[i-2])+int(temp[i-1])+int(temp[i]):
			j=j+1
	print("Number of increments:",j)