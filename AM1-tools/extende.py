#cuidado com estados nao conexos.

def extractcut(string):
	base='mopac-opt'
	LL = len(base)
	oks=''
	while string[LL] != '.':
		oks=oks+string[LL]
		LL+=1
	return oks

def imprime(vet):
	string = ''
	for i in range(len(vet)):
		string += str(vet[i])+ ''
	return string

def conjuglength(vet):
	L = 0
	i = 0
	Lmax = 0
	while i < len(vet):
		if vet[i] ==  1:
			L=0
			while vet[i] != 0:
				L += 1					
				i += 1
				if L > Lmax:
					Lmax = L				
				if i == len(vet): 
					break
		i+=1
	return Lmax


import sys

name = sys.argv[1]
nring = int(sys.argv[2])
Slim = int(sys.argv[3])

fullchain = 30
#print name
cutid = int(extractcut(name))
print cutid

arq = file(name, 'r').readlines()

i=2
while i < len(arq):
	Nconj=0
	if len(arq[i].split()) > 0:
		if arq[i].split()[0] == '#' and int(arq[i].split()[6]) <= Slim:
			energy = arq[i].split()[2]
			i+=1
			vet    = []
			vetone = []
			for k in range(cutid): 
				vetone.append( 'X' )

			for j in range(i,i+nring):
				vet.append( float(arq[j].split()[1]) )
				if float(arq[j].split()[1]) >= 0.05:
					vetone.append(1)
					Nconj += 1
				else:
					vetone.append(0)
			for k in range(nring+cutid,fullchain): 
				vetone.append( 'X' )

			print vetone
			print 'lcheck::', len(vetone)

#			exit()
			print 'vet:',vet
			print 'energy:', energy
			print 'LxE:', Nconj, energy
			print 'vetone: '+ imprime(vetone)
			print 'vetflt: '+ imprime(vet)
#			exit()
	i+=1		
