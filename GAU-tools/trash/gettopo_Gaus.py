def hlink(vec,types):
	stat = 0
	for el in vec:
		if types[el] == 'H':
			stat = 1
	return stat

def genmat(n,m):
	mat = []
	for i in range(n):
		mat.append([])
		for j in range(m):	
			mat[i].append(0)
	return mat

def genvec(n):
	vec = []
	for i in range(n):
		vec.append([])
	return vec


from os import system
import sys
name = sys.argv[1]
Nat = int(sys.argv[2])

print 'starting gettopo, Nat==', Nat

#indices dos enxofres
system('grep HETATM '+name+' > .hetatm')
arq = file('.hetatm','r').readlines()

types = genvec(Nat)
S = []
for line in arq:
#	print line.split()[1], line.split()[2]
	typ  = line.split()[2]
	print typ
	atid = int(line.split()[1])-1
	types[atid] = typ
	if typ == 'S':
		S.append(atid)

#print S, len(S)

#analisa conexoes
system('grep CONECT '+name+' > .conect')
arq = file('.conect','r').readlines()

conect = genvec(Nat)

for line in arq:
	nois = line.split()
	head = int(nois[1])-1
	for i in range(2,len(nois)):
		link = int(nois[i])-1
		#print head, link
		conect[head].append(link)

#conect[ head ][ links ]
#check da matriz de conectividade
matrix = file('matrix.mat', 'w')
for i in range(Nat):
	matrix.write(str(i+1)+'| ')
	for con in conect[i]:
		matrix.write(str(con+1)+' ')
	matrix.write('\n')

print S
#exit()
#print conect[S[0]], S[0]
#exit()

for head in S:
	print head+1,
	for i in range(len(conect[head])):
		print conect[head][i]+1, 
		for CS in conect[conect[head][i]]:
			if CS != head and types[CS] == 'C' and hlink(conect[CS],types) == 1:
				print CS+1,
				print '<-- CB',
#			if CS != head and types[CS] == 'C' and hlink(conect[CS],types) != 1:
#				print CS+1,
#				print '<-- CA',


## tentando achar o carbono alpha_

#				print '\n', conect[CS]
#				exit()

	print 
#	exit()

matrix.close()
