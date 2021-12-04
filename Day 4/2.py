
class Board:
	def __init__(self, numbers):
		self.won = False
		self.board = []
		self.markedBoard = [[1 for col in range(5)] for row in range(5)]
		for number in numbers:
			number = number.replace("\n","")
			self.board.append([int(number[0:2]),int(number[3:5]),int(number[6:8]),int(number[9:11]),int(number[12:14])])

	def AnnouncedNumber(self,value):
		for i in range(5):
			for j in range(5):
				if self.board[i][j]==value:
					self.markedBoard[i][j]=0
					# print("Number found at position",i,j)
					# print(self.board)
					# print(self.markedBoard)
		return self.checkWin(value)

	def checkWin(self,value):
		self.winningNumbers = []
		self.lastNumber = value 
		#Rows
		for row in range(5):
			if sum(self.markedBoard[row])==0:
				self.won = True
				self.winningNumbers = self.board[row]
				return True

		#Columns
		for i in range(5):
			j=0
			self.winningNumbers = []
			for row in range(5):
				if self.markedBoard[row][i]==0:
					j=j+1
					self.winningNumbers.append(self.board[row][i])
				#In case of win
				if j==5:
					self.won = True
					return True

		#In case of lose
		return 0

	def printBoards(self):
		print(self.board)
		print(self.markedBoard)
		print("Winning numbers")
		print(self.winningNumbers)

	def calculatePoints(self):

		otherNumbers = 0
		for i in range(5):
			for j in range(5):
				otherNumbers += self.board[i][j] * self.markedBoard[i][j]


		print(self.lastNumber)
		print(self.lastNumber*otherNumbers)




#Get first line
with open("input.txt", "r") as f:
	numbers = f.readline().replace("\n","").split(",")

	content = f.readlines()
	boardList = []
	for i in range(1,len(content),6):
		boardList.append(Board(content[i:i+5]))

	#Running numbers and checking for winner
	winner= False
	for number in numbers:
			print("len",len(boardList))
			print("New Number:",number)
			for board in boardList:
				if not board.won:
					board.AnnouncedNumber(int(number))
					board.printBoards()
					board.calculatePoints()
				
				
