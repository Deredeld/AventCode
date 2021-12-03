with open("input.txt", "r") as f:
	#Declare arrays
	ones = [0] * 12
	zeros = [0] * 12


	#Read file
	temp = f.read().splitlines()
	
	for line in temp:
		for bit in range(0,len(line)):
			if line[bit]=="0":
				zeros[bit] =zeros[bit]+1
			else:
				ones[bit] =ones[bit]+1
	
	gamma = [0]*12
	epsilon = [0]*12

	for bit in range(0,len(zeros)):
		gamma[bit] = str(int(zeros[bit]< ones[bit]))
		epsilon[bit] = str(int(zeros[bit]> ones[bit]))
	result =  int("".join(gamma),2) * int("".join(epsilon),2)
	print(zeros)
	print(ones)
	print(result)