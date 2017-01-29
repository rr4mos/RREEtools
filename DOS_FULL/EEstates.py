from os import system

system("grep ' Alpha  occ. eigenvalues -- ' *.log > .alpha")

arq = file('.alpha', 'r').readlines()


energy = []
for line in arq:
	splited=line.split()
	for i in range(5,len(splited)):
		energy.append(splited[i])
	
#print energy
homo = len(energy)

print '#homo',float(energy[homo-1])*27.211396132
print '#occupied states'

#print energy


for i in range(len(energy)):
	print i, float(energy[homo-i-1])*27.211396132
