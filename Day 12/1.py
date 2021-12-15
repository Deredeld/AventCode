
class Node():
	def __init__(self,name,connection):
		self.name = name
		self.isSmall = name.islower()
		self.isStart = name == "start"
		self.isEnd = name == "end"
		self.connections = []
		self.addConnection(connection)

	def addConnection(self,name):
		#print("--Adding",name,"to node",self.name)
		if name==self.name:
			print("ggg",name)
		if name not in self.connections:
			self.connections.append(name)

	def __str__(self):
		return "Name: " + self.name + " |small:" + str(self.isSmall) + " |Connections:" + ";".join(self.connections)



class Cave():
	def __init__(self):
		self.nodes = []
		self.listOfpaths = []

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


	def getStart(self):
		for node in self.nodes:
			if node.name == "start":
				return node

	def getNodeFromName(self,name):
		for node in self.nodes:
			if node.name == name:
				return node
		print("cant find",name)

	def makePath(self,path,node):
		print("makePath",path,node)
		temppath = path.copy()

		if node.isEnd:
			temppath.append("end")
			self.listOfpaths.append(temppath)

		elif temppath and node.name in temppath and node.isSmall and not node.isStart:
			print("Is small")
		else:
			print("Else")
			temppath.append(node.name)
			for node in node.connections:
				if  node != "start":
					newNode = self.getNodeFromName(node)
					self.makePath(temppath,newNode)


		



with open("input.txt", "r") as f:
	cave = Cave()
	for line in f.read().splitlines():
		nodes = line.split("-")
		cave.addNode(nodes[0],nodes[1])

	cave.printCave()
	print("Start process")
	cave.makePath([],cave.getStart())
	for p in cave.listOfpaths:
		print(p)

	print("All",len(cave.listOfpaths),"paths:")
