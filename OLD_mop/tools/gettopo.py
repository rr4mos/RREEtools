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

Nat = 142

#indices dos enxofres
system('grep HETATM '+name+' > .hetatm')
arq = file('.hetatm','r').readlines()

types = genvec(Nat)
S = []
for line in arq:
#	print line.split()[1], line.split()[2]
	typ  = line.split()[2]
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
	matrix.write(str(i)+'| ')
	for con in conect[i]:
		matrix.write(str(con)+' ')
	matrix.write('\n')

for head in S:
	print head+1,
	for i in range(len(conect[head])):
		print conect[head][i]+1, 
		for CS in conect[conect[head][i]]:
			if CS != head and types[CS] == 'C' and hlink(conect[CS],types) == 1:
				print CS+1,


	print 
#	exit()

matrix.close()
