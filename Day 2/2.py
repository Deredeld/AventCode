with open("input.txt", "r") as f:
	depth = 0
	forward = 0
	aim = 0
	temp = f.read().splitlines()
	print(temp)
	for line in temp:
		if line.startswith("f"):
			forward += int(line[-1])
			depth += aim*int(line[-1])
		elif line.startswith("u"):
			aim -= int(line[-1])
		else:
			aim += int(line[-1])

	print(forward)
	print(depth)
	print(aim)
	print("Final result:",forward*depth)
