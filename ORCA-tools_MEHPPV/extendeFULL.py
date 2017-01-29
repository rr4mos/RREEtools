#cuidado com estados nao conexos.

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

cutid = 0#int(sys.argv[1])
name = sys.argv[2]
nring = int(sys.argv[3])
Slim = int(sys.argv[4])  
#name: nome do arquivo "-ORBITAIS"
#nring: num. de aneis do patch
#Slim: num. de orbitais analisados


fullchain = 9
print "Full Chain (fixed): 9"
print "Slim: ", Slim
criterio = float(1.0/nring)
print "criterio de ocupacao:",criterio

print 'name:',name
print 'cutid:', cutid
#exit()

arq = file(name, 'r').readlines()

i=2
while i < len(arq):
	Nconj=0
	if len(arq[i].split()) > 0:
		if arq[i].split()[0] == '#' and int(arq[i].split()[6]) <= Slim:
			energy = arq[i].split()[2]
			idenergy = arq[i].split()[4]+arq[i].split()[5]+' '+arq[i].split()[6]
#			print energy, idenergy
			i+=1
			vet    = []
			vetone = []
			for k in range(cutid): 
				vetone.append( 'X' )

			for j in range(i,i+nring):
				vet.append( float(arq[j].split()[1]) )
				if float(arq[j].split()[1]) >= criterio:
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
			print 'orb:', idenergy			
			print 'LxE:', Nconj, energy
			print 'vetone: '+ imprime(vetone)
			print 'vetflt: '+ imprime(vet)
#			exit()
	i+=1		
