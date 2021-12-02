with open("input.txt", "r") as f:
	depth = 0
	forward = 0
	temp = f.read().splitlines()
	print(temp)
	for line in temp:
		if line.startswith("f"):
			forward += int(line[-1])
		elif line.startswith("u"):
			depth -= int(line[-1])
		else:
			depth += int(line[-1])

	print(forward)
	print(depth)
	print("Final result:",forward*depth)
