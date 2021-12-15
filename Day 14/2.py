import re
import collections


def split(word):
    return [char for char in word[0:-1]]


def addLetter(di,l,number):
	if l in di.keys():
		di[l] +=number
	else:
		di[l] = number

def addPair(di,l,number):
	if l in di.keys():
		di[l] += number
	else:
		di[l] = number


with open("input.txt", "r") as f:
	base = split(f.readline())
	
	listOfLetters = {}
	#Get list of letters
	for l in base:
		addLetter(listOfLetters,l,1)

	

	#Get list of pairs
	listOfPairs = {}
	for i in range(len(base)-1):
		addPair(listOfPairs,base[i]+base[i+1],1)

	#Get list of transformations
	listMarks = []
	for line in f.read().splitlines():
		nodes = re.search(r"([A-Z]*?) -> ([A-Z])",line)
		if nodes:
			listMarks.append([nodes.group(1),nodes.group(2)])

	print(collections.Counter(listOfPairs))
	print(collections.Counter(listOfLetters))
	for i in range(40):
		print(i)
			#Step
		newList = listOfPairs.copy()
		for m in listMarks:
			numberOfOccurences=0
			#If transformation as a pair
			#Create 2 new pairs and add number
			if m[0] in listOfPairs.keys():
				p1 = m[0][0]+m[1]
				p2 = m[1]+m[0][1]
				numberOfOccurences = listOfPairs[m[0]]

				print("---",m[0],m[1],"-> New pairs",p1,p2,"times",numberOfOccurences)

				addLetter(listOfLetters,m[1],numberOfOccurences)
				#Add new pairs remove old one

				addPair(newList,p1,numberOfOccurences)
				addPair(newList,p2,numberOfOccurences)
				addPair(newList,m[0],-numberOfOccurences)
		listOfPairs = newList.copy()
		print(collections.Counter(listOfPairs))
		print(listOfLetters)
	m = listOfLetters
	print(m[max(m, key=m.get)]-m[min(m, key=m.get)])