
class Node():
	def __init__(self,name,connection):
		self.name = name
		self.isSmall = name.islower()
		self.isStart = name == "start"
		self.isEnd = name == "end"
		self.connections = []
		self.addConnection(connection)
		self.passedThrough = 0
		if name == "start" or name == "end":
			self.passedThrough=2

	def addConnection(self,name):
		#print("--Adding",name,"to node",self.name)
		if name==self.name:
			print("ggg",name)
		if name not in self.connections:
			self.connections.append(name)

	def setConnections(self,c):
		self.connections = c

	def __str__(self):
		return "Name: " + self.name + " |small:" + str(self.isSmall) + " |passedThrough:" + str(self.passedThrough) + " |Connections:" + ";".join(self.connections)

class Path():

	def __init__(self,oldPath):
		self.path = []
		for i in oldPath:
			self.path.append(i)


#Add a Node, if the end return True
	def addNode(self,node):
		print("+++Adding node",node)
		self.path.append(node)
		print(self)
		if node.isEnd:
			return True
		return False

	def getOldNodeFromName(self,name):
		for node in self.path:
			if node.name == name:
				return node
		return None
			


	def __str__(self):
		print("--Printing path")
		nodes = ""
		for node in self.path:
			nodes= nodes+ "," + node.name
		return nodes



class Cave():
	def __init__(self):
		self.nodes = []
		self.listOfpaths = []
		self.listOfEndedpaths = []

	def addNode(self,first,second):
		print(first,second)
		for node in self.nodes:
			if node.name == first:
				node.addConnection(second)	

				for secondNode in self.nodes:
					if secondNode.name == second:
					#The first node and second node are already in the list
						secondNode.addConnection(first)
						return 0
				#The second node is not found and added to the list
				self.nodes.append(Node(second,first))
				return 0

		#The first node is not found so we add it to the list and check for the second 
		self.nodes.append(Node(first,second))
		for secondNode in self.nodes:
					if secondNode.name == second:
						secondNode.addConnection(first)
						return 0

		#If the second node is not in the list create it
		self.nodes.append(Node(second,first))

	def printCave(self):
		for node in self.nodes:
			print(node)

	def printPaths(self):
		for p in self.listOfpaths:
			print(p)

	def getStart(self):
		for node in self.nodes:
			if node.name == "start":
				return node

	def getFreshNodeFromName(self,name):
		for node in self.nodes:
			if node.name == name:
				return node
		print("cant find",name)

	def makePath(self,Originalpath,node):
		print("--------Making path")
		print(node)
		print("Current path")
		print(Originalpath)
		print("Others")
		self.printPaths()
		print("-------------------")
		path = Path(Originalpath.path)
		
		self.listOfpaths.append(path)
		lastNode = path.path[-1]
		if lastNode.name == "end":
			self.listOfEndedpaths.append(path)
			print("End of path")
		#If node is 2 or more or start

		elif not lastNode.isStart and (lastNode.isSmall and lastNode.passedThrough==2):
			#print(lastNode)
			print("Is rejected")
		else:
			#print("Else")
			for node in lastNode.connections:
				#Try to find node in path
				newNode = path.getOldNodeFromName(node)
				#If no node found
				if not newNode:
					tempNode = self.getFreshNodeFromName(node)
					newNode  = Node(tempNode.name,"")
					newNode.setConnections(tempNode.connections.copy())
				if newNode.name != "start":
					#print("DIFF START")
					if (newNode.isSmall and newNode.passedThrough<2):
						if newNode.isSmall:
							#print("ADDING PASSAGE")
							newNode.passedThrough+=1
					path.addNode(newNode)
					self.makePath(path,newNode)

		



with open("input.txt", "r") as f:
	cave = Cave()
	for line in f.read().splitlines():
		nodes = line.split("-")
		cave.addNode(nodes[0],nodes[1])

	print("Start process")
	cave.makePath(Path([cave.getStart()]),cave.getStart())


	print("All",len(cave.listOfEndedpaths),"paths")

	for path in cave.listOfEndedpaths:
		print(path)
