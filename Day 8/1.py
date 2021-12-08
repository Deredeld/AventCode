with open("input.txt", "r") as f:
	count = 0
	for line in f.read().splitlines():
			for word in (line.split("|")[1].split(" ")):
				#if 7  or 4 or 1 or 8
				if len(word)==3 or len(word)==4 or len(word)==2 or len(word)==7: count+=1
	print(count)