import itertools


class Digicode:
	def __init__(self):
	#Declaring a matrix for each number and each possible letter/segment they might have
		self.s = [[] for row in range(7)]

	#List of each letters for each numbers
		self.numbers = [[] for row in range(10)]

		self.sixesSolved= 0

	def printAll(self):
		for i in range(10):
			print("Number",str(i),"is",sorted(self.numbers[i]))
		for i in range(7):
			print("Segment",str(i),"is",sorted(self.s[i]))

	def newInput(self,input):
		for word in input:
			word  = list(word)
			numberOfSegments = len(word)
			if numberOfSegments==1:
				print("error")
			#Number is a 1
			elif numberOfSegments==2:
				self.numbers[1]=word
			#Number is a 4
			elif numberOfSegments==4:
				self.numbers[4]=word
			#Number is a 7
			elif numberOfSegments==3:
				self.numbers[7]=word
			#Number is a 8
			elif numberOfSegments==7:
				self.numbers[8]=word

	def subLists(self,A,B):
		return [item for item in sorted(A) if item not in sorted(B)]

	def loopSixes(self,input):
		#Part 1
		self.printAll()
		if self.sixesSolved == 0:
			for letters in input:
				#If we have a 6 or 9 or 0
					#We have a 6 and the 2 segment is 8-6
					if len(self.subLists(letters,self.numbers[1]))==5:
						self.numbers[6]=letters
						self.s[2] = self.subLists(self.numbers[8],letters)
					#if we have a 9 the 4 segment is 8-9
					elif len(self.subLists(letters,self.numbers[4]))==2:
						self.numbers[9]=letters
						self.s[4] = self.subLists(self.numbers[8],letters)
					else:
						self.numbers[0]=letters
						self.s[3] = self.subLists(self.numbers[8],self.numbers[0])
						#Get segment 3 (8-0)
						
						
			self.sixesSolved=2

			
						
	
	def workoutSegments(self,input):
		#Segment 0 is letters from 7 minus letters from 1
		self.s[0] = self.subLists(self.numbers[7],self.numbers[1])

		#length 6 words
		sixes = []
		for word in input:
			if len(word)==6:
				sixes.append(list(word))
		self.loopSixes(sixes)
		for word in input:
			letters = list(word)
			#if 7 then sub 2 known values to guess segment 6
			if(len(letters) ==3 and self.s[2]):
				temp = self.subLists(letters,self.s[0])
				self.s[5] = self.subLists(temp,self.s[2])
		self.loopSixes(sixes)

		for word in input:
				if len(word)==4:
					print("her")
					temp = self.s[2]+self.s[3]+self.s[5]
					self.s[1] = self.subLists(self.numbers[4],temp)
					self.sixesSolved=3


		#Final solve, missing segment
		knownSegments = list(itertools.chain.from_iterable(self.s))
		print(knownSegments)
		print(self.subLists('abcdefg',sorted(knownSegments)))
		self.s[6] = self.subLists('abcdefg',knownSegments)

		self.numbers[2]=self.s[0]+self.s[2]+self.s[3]+self.s[4]+self.s[6]
		self.numbers[3]=self.s[0]+self.s[2]+self.s[3]+self.s[5]+self.s[6]
		self.numbers[5]=self.s[0]+self.s[1]+self.s[3]+self.s[5]+self.s[6]

	def decodeEnd(self,input):
		print("Decoding")
		finalNumber = []
		for i in range(len(input)):
			if len(input[i])>0:
				for number in self.numbers:
					if str("".join(sorted(input[i])))=="".join(sorted(number)):
						print("gggggggggggg")
						print(self.numbers.index(number),input[i])
						finalNumber.append(self.numbers.index(number))
		finalNumber = int(''.join(str(x) for x in finalNumber))
		print(finalNumber)
		return finalNumber




with open("input.txt", "r") as f:
	count = 0
	digicode = Digicode()
	for line in f.read().splitlines():
		new = line.split("|")[0].split(" ")
		digicode.newInput(new)
		digicode.workoutSegments(new)
		digicode.printAll()
		count+=digicode.decodeEnd(line.split("|")[1].split(" "))
		digicode = Digicode()
	print(count)
