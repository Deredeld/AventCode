

#Used to count the numbers of 1 and 0 for all the numbers in the list for a certain position and result the winner 
def countOnesAndZeros(listValues,position):
	#Declare arrays
	ones = 0
	zeros = 0
	for line in listValues:
		if line[position]=="0":
			zeros =zeros+1
		else:
			ones = ones+1
	return int(zeros <= ones)


def getMostBits(listSup,listInf,position,result):
	print("Begin main",position)
	if len(listSup)==1:
		print("-------End sup")
		result[0] = listSup[0]
	if len(listInf)==1:
		print("-------End inf")
		result[1] = listInf[0]
	if position == 12 or (len(listSup)==1 and len(listInf)==1 ):
		print(int(result[0],2) * int(result[1],2) )
	else:

		mostCommonSup = countOnesAndZeros(listSup,position)
		mostCommonInf = countOnesAndZeros(listInf,position)

		#Declaring new lists
		newlistSup = []
		newlistInf = []
		#Creating a new list for superior values
		for value in range(0,len(listSup)):
			if int(listSup[value][position]) == int(mostCommonSup):
				newlistSup.append(listSup[value])

		#Creating a new list for inferior values
		for value in range(0,len(listInf)):
			if int(listInf[value][position]) != mostCommonInf:
				newlistInf.append(listInf[value])

		print("Sup",len(listSup))
		print("Inf",len(listSup))
		getMostBits(newlistSup,newlistInf,position+1,result)









with open("input.txt", "r") as f:
	result = [0,0]
	#Read file
	sup = f.read().splitlines()
	inf = sup[:]
	getMostBits(sup,inf,0,result)