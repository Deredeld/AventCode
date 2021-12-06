from collections import Counter
import time

#Get first line
with open("input.txt", "r") as f:
	numbers = f.readline().replace("\n","").split(",")

	#Create empty dict
	dic = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
	dic.update(dict(Counter(numbers)))

	start_time = time.time()
	for i in range (256):
		#Temp value to cycle values
		temp = dic["0"]
		for j in range(8):
				dic[str(j)]=dic[str(j+1)]
		dic["6"]+=temp
		dic["8"]=temp
	print(sum(dic.values()))
	print("--- %s seconds ---" % (time.time() - start_time))
