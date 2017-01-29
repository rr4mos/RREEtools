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

def genvec2(n):
	vec = []
	for i in range(n):
		vec.append(0)
	return vec


from os import system
import sys
name = sys.argv[1]
Nat = int(sys.argv[2])
Nrings = int(sys.argv[3])

#print 'starting gettopo, name==', name
#print 'starting gettopo, Nat==', Nat

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
matrix.close()

#definindo os indices de atomos dos aneis 
rings = []
for head in S:
	Sstring = []
	Sstring.append(head)
	for i in range(len(conect[head])):
		Sstring.append(conect[head][i]) 
		for CS in conect[conect[head][i]]:
			if CS != head and types[CS] == 'C' and hlink(conect[CS],types) == 1:
				Sstring.append(CS)


	rings.append(Sstring) 

#determinando ordenamento dos aneis
links = []
linkdock = []
repete = []
extconect =genmat(len(rings),len(rings))
k = 0
for string in rings:
	for i in string:
		if i in links:
			extconect[linkdock[links.index(i)]][k] = 1
			extconect[k][linkdock[links.index(i)]] = 1
		for j in conect[i]:
			if j not in string:
				if types[j] != 'H':
					links.append(j)
					linkdock.append(k)		
	k += 1
		
#print 'linkdock:', linkdock
#print 'total de aneis', len(rings), k

struct=file('.struct'+name, 'w')
for i in range(len(extconect[0])):
	for j in range(len(extconect[0])):
		struct.write(str(extconect[i][j])+ ' ')
	struct.write('\n')
struct.close()

for i in range(Nrings):
	count1 = 0
	for j in range(Nrings):
		if extconect[i][j] == 1:
			count1+= 1
	if count1 == 1:
		break 

current = i
before = 9999
for i in range(Nrings):
	imprime = ''
	for rg in rings[current]:
		imprime += str('{:5d}'.format(rg+1)) + ' '
	print imprime

	for j in range(Nrings):
#		print extconect[current][j]
		if extconect[current][j] == 1 and j != before:
#			print 'entrou', j
			before = current
			current = j
			break
#			print 'current', current
#			print current
	



