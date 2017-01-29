from math import sqrt
import sys

def genvec(n):
	vec = []
	for i in range(n):
		vec.append(0.00)
	return vec

name = sys.argv[1]
arq = file(name, 'r').readlines()

#com 10#
#n = 222
#nhomo = 121
#nlim = nhomo - 2

#com 20#
n = 442
nhomo = 241
nlim = nhomo - 4

e = genvec(n)
nspecs = 0
i=1
for line in arq:
	e[i%n]= e[i%n]+float(line.split()[0])
	if i%n == 0:
		nspecs += 1 
	i+=1	

print '# no de espectros::',nspecs
print '# no de estados em cada espectro::', n

for i in range(0,n):
	e[i]= e[i]/nspecs
#print e

edge = file(name+'-edge.dat', 'w')
var = genvec(n)
i=1
for line in arq:
	var = e[i%n] - float(line.split()[0])
	
	if i%n > nlim and i%n <= nhomo:
		edge.write( str(i%n)+' '+ str(var)+'  '+ str(e[i%n])+ '\n')
	if i%n != 0 and i%n <= nhomo:
		print str(i%n)+' '+ str(var)+'  '+ str(e[i%n])
	i+=1



