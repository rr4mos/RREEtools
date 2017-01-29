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
		for j in range(5):
			L.append(float(check[len(check)-1-j]))
			#print L
		MOS.append(L)
		il+=1
		check=arq[il].split()	

	return MOS


def getlabels(il,arq,t):
	check=arq[il].split()
	LBs = []
	for k in range(t):
		if check[0] not in LBs:
			LBs.append(check[0])
#		else:
#			print #check[0], check[1]
		il += 1
		check=arq[il].split()
	return LBs

def cleanLB(strgLst):
#	print strgLst
	strgLstOK=[]
	for strg in strgLst:
		strg=strg[len(strg)-1]
		strgLstOK.append(strg)
	return strgLstOK


orbs631 = {'S':19,'C':15,'H':2}
orbsAM1 = {'S':5,'C':5,'H':1}
orbsZD = {'O':4,'C':4,'H':1}

Base = orbsZD

arq   = file(arqname+".out",'r').readlines()
#espec = file(arqname+'-ESPEC','w')


ecount = 0
i = 0
EV = genmat(Nat)
ES = []
leitura = 0

E  = []
while i < len(arq):
	check=arq[i].split()
#	print check
#	print len(check)
	if len(check) > 0:
		if check[0] == 'ORBITAL':
#			print check
			i+=4
			check=arq[i].split()
			nhomo = 1
			while check[1] == "2.0000":
#				print check
				if check[1]!='0.0000':
					E.append(check[3])			
				i+=1
				check=arq[i].split()

			nhomo=len(E)-1
#			print 'HOMO:',nhomo,E[nhomo]		

		if check[0] == 'MOLECULAR':
			i+=2 			
			check=arq[i].split()
#			print check
			while str(nhomo) not in check:
				i+=Norbs+4
#				print '#',i
				if i >= len(arq): 
					print 'ERRO NO NUM DE ORBITAIS.......'					
					exit()

				check=arq[i].split()
#				print check
			col=check.index(str(nhomo))+2
			i+=4
#			print arq[i].split()
			#print "Eigenvectors"
			MOS = getcoefs(i,arq,Norbs)					
#			print MOS
			#print "Labels"
			LBs = getlabels(i,arq,Norbs)
#			print LBs
#			print 'Natoms', len(LBs)
			LBs=cleanLB(LBs)
#			print LBs
#			print len(LBs)
			break

	i+=1
#print LBs, len(LBs) 
#print '*******'

#print E
print '#HOMO:', float(E[nhomo])
print '#LUMO: not taken'
print ''

#for i in range(Norbs):
#	print 'HOMOCOEF', MOS[i][0]
#exit()

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




orbats=file('ORBITAIS-full','w')
st_id=0
for ST in EV:
	orbats.write('\n\n#HOMO-' +str(st_id) + '\n')
	Sest = sum(ST)
	orbats.write('#Norma = '+str(Sest)+'\n\n')

	for i in range(Nat):
		orbats.write( str(i+1) + ' '+str(LBs[i])+' '+str(ST[i]/Sest) + '\n')
	st_id+=1

orbats.close()
#get backbone



back = file(arqname+'-RINGS','r').readlines()
backbone = []
i = 0
for line in back:
	backbone.append([])
	for at in line.split():
		backbone[i].append(int(at))
	i+=1
print backbone

for i in range(NO):
		print "# energy:",float(E[nhomo-i]), ':: HOMO -', i
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

