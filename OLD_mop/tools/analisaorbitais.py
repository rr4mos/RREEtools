import sys
#uso analisaorbitais.py nome num.atomos homo.level 

arqname = sys.argv[1]
Nat     = int(sys.argv[2])
homo    = int(sys.argv[3]) - 1
Norbs   = 10

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

orbs = {'S':4,'C':4,'H':1}

arq   = file(arqname,'r').readlines()
espec = file('ESPEC-'+ arqname,'w')

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
				espec.write("1  "+str(val)   +'\n')
				espec.write("2  "+str(val)   +'\n')
				ecount += 1
				espec.write("#  "+str(ecount)+'\n\n')
	
			#estah numa faixa dos autovetores
			i+=3
			line = arq[i].split()
			n  = int(line[2])
			tp = line[1]
			EV2=[]
			while n < Nat:				
				if tp != 'X':
					EV2 = getcoefs(i,arq,orbs[tp])
					for each in EV2:
						EV[n-1].append(each)
#				print '\n',n,tp,orbs[tp]
#				print EV2

				i=i+orbs[tp]+1

				if len(arq[i].split()) < 1:
					i+=1
				line = arq[i].split()
				n  = int(line[2])
				tp = line[1]
#pegando o ultimo
			if tp != 'X':
				EV2 = getcoefs(i,arq,orbs[tp])
				for each in EV2:
					EV[n-1].append(each)
#

	i+=1
espec.close()

#checks de consistencia :: ok, 19.08.13

Nspec = len(ES)

#checando dimensao dos autovetores
#for i in range(len(EV)):
#	print len(EV[i]),i+1

#checando norma 1 dos estados quanticos (se inclui todos)
#(--> norm.dat)
norm = file('norm.dat','w')
for e in range(Nspec):
	soma = 0.0
	for i in range(Nat):
		soma=soma+EV[i][e]
	norm.write( str(e)+'  '+str(soma)+'\n')
norm.close()


#ir do homo pra baixo ateh ter os estados cobertos sobre toda a estrutura
#acumular nos aneis 

print '#HOMO:',ES[homo]
print '#LUMO:',ES[homo+1]
print 

#get backbone

back = file(arqname+'.pdb-RINGS','r').readlines()
backbone = []
i = 0
for line in back:
	backbone.append([])
	for at in line.split():
		backbone[i].append(int(at))
	i+=1
#print backbone

for i in range(Norbs):
		print "# energy:",ES[homo-i], ':: HOMO -', i
		ringid = 1
		for ring in backbone:		
			soma = 0.0
#			print 'anel:', ring
			for at in ring:	
#				print at
				soma = soma + EV[at-1][homo-i]
			print ringid, soma
			ringid += 1
		print

