Norbs = 20

def genvec(n):
	vec = []
	for i in range(n):
		vec.append(0.00)
	return vec

def genmat(n):
	vec = []
	for i in range(n):
		vec.append([])
	return vec

def getcoefs(il,arq,t):
	CC = []
	nsp = len(arq[il].split())-3
	Csum2 = genvec(nsp)
	i = 0
	while i < t:
		check = len(arq[il+i].split())
		#corrige zica do mopac
		if check < nsp:
			i+=1
		line = arq[il+i].split()
#		print line
		for j in range(nsp):
			Csum2[j]=Csum2[j]+float(line[j+3])**2
		i+=1
	return Csum2


import sys
arqname = sys.argv[1]
Nat = 142
orbs = {'S':4,'C':4,'H':1}


arq   = file(arqname,'r').readlines()

ecount = 0
i = 0
EV = genmat(Nat)
ES = []
leitura = 0
while i < len(arq):
	check=arq[i].split()
#	print check
	if len(check) > 0:
		if check[0] == 'ROOT':
			leitura += 1
			i+=2
			#encontrou autovalores
			for val in arq[i].split():
				ES.append(val)
				print str(val)
				ecount += 1
	

	i+=1


