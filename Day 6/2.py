from collections import Counter

#Get first line
with open("input.txt", "r") as f:
	numbers = f.readline().replace("\n","").split(",")

	#Create empty dict
	dic = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
	dic.update(dict(Counter(numbers)))

	for i in range (256):
		#Temp value to cycle values
		temp = 0
		temp2 = 0
		for j in range(8,-1,-1):
			if j==0:
				temp = dic[str(j)]
				dic[str(j)]=temp2
				dic["6"]+=temp
				dic["8"]=temp
			else:
				temp = dic[str(j)]
				dic[str(j)]=temp2
				temp2 = temp
	print(sum(dic.values()))