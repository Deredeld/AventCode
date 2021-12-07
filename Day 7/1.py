import statistics

#Get first line
with open("input.txt", "r") as f:
	numbers = list(map(int,f.readline().replace("\n","").split(",")))
	med = statistics.median(numbers)
	sum = 0
	for number in numbers:
		sum+=abs(med-number)
	print(sum)