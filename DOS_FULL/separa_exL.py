def adj(string):
	L=2
	while len(string)<L:
		string ='0'+string
	return string

from os import system

system('sort -k 2 -n Mergeespectro.dat > .sort')

arq = file('.sort','r').readlines()

Lprev=''
for line in arq:
	if line.split()[0]!="#orbitais":
		
		L=line.split()[1]
		E=line.split()[2]
	
		if L != Lprev:
			output=file(adj(L)+'_E.dat', 'w')
			output.write(E+'\n')			
			Lprev=L
		else:
			output.write(E+'\n')
			
