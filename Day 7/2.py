import statistics
import math
import time

def CalculateCost(number,aim):
	 distance = abs(number-aim)
	 cost = 0
	 for i in range(1,distance+1):
	 	cost += i
	 return cost

#Get first line
with open("input.txt", "r") as f:
	numbers = list(map(int,f.readline().replace("\n","").split(",")))
	med = int(statistics.median(numbers))
	bestCost = 9999999999999
	start_time = time.time()

	#CalculateForNextBest
	position = []
	Values = []
	newMed = med
	for i in range(0,max(numbers)):
		newCost = 0
		for number in numbers:
			newCost+=CalculateCost(number,i)
		if newCost<bestCost:
			bestCost=newCost
			newMed=i
		else:
			break
	print(bestCost)
	print(newMed)
	print("--- %s seconds ---" % (time.time() - start_time))