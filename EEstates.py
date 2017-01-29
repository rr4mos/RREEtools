from os import system
import sys


Nmax = int(sys.argv[1])
flat = int(sys.argv[2])

if flat == 0:

	system("grep ' Alpha  occ. eigenvalues -- ' *.log > .alpha")
	system("grep ' Alpha virt. eigenvalues -- ' *.log > .valpha")

arq = file('.alpha', 'r').readlines()

energy = []
for line in arq:
	splited=line.split()
	for i in range(5,len(splited)):
		energy.append(splited[i])

arq = file('.valpha', 'r').readlines()


energyV = []
for line in arq:
	splited=line.split()
	for i in range(5,len(splited)):
		energyV.append(splited[i])

homo = len(energy)
lumo = 0

print ' #   homo-   lumo+'

for i in range(Nmax+1):

	print '{:2d}'.format(i), '{:7.3f}'.format(float(energy[homo-i-1])*27.211396132),\
       			         '{:7.3f}'.format(float(energyV[i])      *27.211396132)
