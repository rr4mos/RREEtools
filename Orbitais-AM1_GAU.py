import sys
#uso analisaorbitais.py nome num.atomos homo.level 

arqname = sys.argv[1]
Nat     = int(sys.argv[2])
homo    = int(sys.argv[3]) - 1
Norbs   = 10

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
	#print check
#	MOS = genmat(33) # MOS[1<i<Norbs][HOMO-5<n_orb<HOMO]
	MOS = []
	#print MOS
	for k in range(t):
		L = []
		for j in range(5):
			L.append(float(check[len(check)-1-j]))
			#print L
		MOS.append(L)
		il+=1
		check=arq[il].split()	

		#print MOS
	return MOS


def getlabels(il,arq,t):
	check=arq[il].split()
	LBs = []
	for k in range(t):
		if len (check) == 9:
			#print check[0], check[1], check[2], check[3]
			LBs.append(check[2])
		else:
			print #check[0], check[1]
		il += 1
		check=arq[il].split()

	return LBs


orbsAM1 = {'S':5,'C':5,'H':1}
orbs631s= {'C':15,'H':2}
#Base = orbsAM1
Base = orbs631s

arq   = file(arqname,'r').readlines()
espec = file('ESPEC-'+ arqname,'w')

ecount = 0
i = 0
EV = genmat(Nat)
ES = []
leitura = 0

EV = []
NO = 5
Norbs = 91
while i < len(arq):
	check=arq[i].split()
	if len(check) > 3:
#		print check[0], check[1]
		if check[0] == 'Eigenvalues' and check[1] == '--':

			#eigenvalues
			#print "Eigenvalues::"
			for k in range(2,2+NO):
				EV.append(check[k])			
			#print EV
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
	print '#Est. :', j
	print '#Parts:', EV2
	print '#Norma:', sum(EV2)
	
	for i in range(len(EV2)):
		print i+1,EV2[i]
	print 





