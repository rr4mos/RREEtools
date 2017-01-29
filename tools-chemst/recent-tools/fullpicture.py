from os import system
import sys

name = sys.argv[1]
numb = sys.argv[2]
system("grep '#' "+ name+"| grep 'XX' > ."+numb)

chain = file('.'+numb).readlines()
fullpic = []
for i in range(30):
	fullpic.append(0)
N=0 #norma

#print fullpic
for line in chain:
	pic= line.split()[0]
	for i in range(0,30):
		
		if pic[i+1] == 'X': 
			fullpic[i]+=0
		else:	
			if pic[i+1] == '0':	
				fullpic[i]+=0
			else:
				fullpic[i]+=1
				N += 1
#		print pic[i+1], fullpic[i]

print '#', N
for i in range(len(fullpic)):
	if fullpic[i] >= 0.05: 
		print 1.0 #float(fullpic[i])/float(N)
	else:
		print 0.0
