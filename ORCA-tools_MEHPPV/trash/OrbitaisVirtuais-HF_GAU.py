import sys
#uso analisaorbitais.py nome num.atomos n.orbitais.atomicos(total) n.orbitais analisados (5)

arqname =     sys.argv[1]
Nat     = int(sys.argv[2])
Norbs 	= int(sys.argv[3])
NO 	= int(sys.argv[4])

#print 'arqname', arqname
#print 'Nat', Nat
#print 'Norbs', Norbs
#print 'NO', NO

def normalize(vec):
	soma = 0.0
	for i in range(len(vec)):
		soma = soma + vec[i]
#	print 'norma:', soma
	for i in range(len(vec)):
		vec[i] = vec[i]/soma

	return vec

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
	check=arq[il].split()
	MOS = []
	for k in range(t):
		L = []
		if len(check) == 7:
			first = 2
		if len(check) == 9:
			first = 4 
		for j in range(first,len(check)):
			L.append(float(check[j]))
#		print L
		MOS.append(L)
		il+=1
		check=arq[il].split()	

#	print MOS
#	exit()
	return MOS


def getlabels(il,arq,t):
	check=arq[il].split()
	LBs = []
	for k in range(t):
		if len (check) == 9:
			#print check[0], check[1], check[2], check[3]
			LBs.append(check[2])
#		else:
#			print #check[0], check[1]
		il += 1
		check=arq[il].split()

	return LBs


orbs631 = {'S':19,'C':15,'H':2}
orbsAM1 = {'S':5,'C':5,'H':1}
Base = orbs631

arq   = file(arqname+".log",'r').readlines()
#espec = file(arqname+'-ESPEC','w')


ecount = 0
i = 0
EV = genmat(Nat)
ES = []
leitura = 0

E  = []
while i < len(arq):
	check=arq[i].split()
	if len(check) > 3:
#		print check[0], check[1]
		if check[0] == 'Eigenvalues' and check[1] == '--':
		    flag=arq[i-1].split()
		    if flag[len(flag)-1] == 'V':
			
			#eigenvalues
			#print "Eigenvalues::"
#			print check
			for k in range(2,7):
				E.append(check[k])	
			i+=1

			#eigenvectors
			#print "Eigenvectors::"
			MOS = getcoefs(i,arq,Norbs)
			
			#print "Labels"
			LBs = getlabels(i,arq,Norbs)
							
			break

	i+=1

#print LBs, len(LBs) 
#print '*******'
#print E
print '#LUMO:', float(E[0])*27.211396132
print ''

EV=[]
for j in range(NO):
	m = 0
	EV2 = []
	for i in range(len(LBs)):
#		print '**base:',LBs[i],Base[LBs[i]]
		Coef2 = 0.0
		for k in range(Base[LBs[i]]):
#			print MOS[m+k][j]
			Coef2+=MOS[m+k][j]**2
		m+=Base[LBs[i]]
		EV2.append(Coef2)
#	print 'numero de atomos', len(EV2)
	EV.append(EV2)
#	print '#Est. :', j
#	print '#Energy:', float(E[4-j])*27.211396132
#	print '#Parts:', EV2
#	print '#Norma:', sum(EV2)
#	print 

#print EV[0][1]

#get backbone

back = file(arqname+'-RINGS','r').readlines()
backbone = []
i = 0
for line in back:
	backbone.append([])
	for at in line.split():
		backbone[i].append(int(at))
	i+=1
#print backbone

for i in range(NO):
		print "# energy:",float(E[i])*27.211396132, ':: LUMO +', i
		ringid = 1
		allsums = []
		for ring in backbone:		
			soma = 0.0
#			print 'anel:', ring
			for at in ring:	
#				print ring
#				print at -1, i
				soma = soma + EV[i][at-1]
			allsums.append(soma)
#			print ringid, soma
			ringid += 1

#		for i in range(len(backbone)):
#			print i+1, allsums[i]
#		print 'xxxxxxxxxxx'
		allsums = normalize(allsums)
		soma = 0.0
		for i in range(len(backbone)):
			print i+1, allsums[i]
			soma = soma + allsums[i]
		print '#check sum:', soma
		print ''

