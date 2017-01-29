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

alpha_list = file('alpha_c.list','r').readlines()
for i in range(len(alpha_list)):
	alpha_list[i]=int(alpha_list[i].split()[0])-1
#	print alpha_list[i]


S = []
for line in arq:
#	print line.split()[1], line.split()[2]
	typ  = line.split()[2]
	atid = int(line.split()[1])-1	
	types[atid] = typ
	if atid in alpha_list:
		S.append(atid)

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

#print conect
#exit()
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
#AQUI EH MUITO ESPECIFICO DA TOPOLOGIA

rings = []
for head in S:
	Sstring = []
	Sstring.append(head)
#	print Sstring
#	print conect[head]
	for atom in conect[head]:
			if types[atom] == 'C':
				Sstring.append(atom) 

	for i in range(len(conect[head])):
		for CS in conect[conect[head][i]]:
				if CS != head and types[CS] == 'C':
#					print types[CS]
					Sstring.append(CS)
#					print Sstring


	Sstring.append(head+3)
#	print Sstring 	
	rings.append(Sstring) 

#	exit()

#print 'RINGS', rings
#print 'Len', len(rings)

#exit()


##determinando ordenamento dos aneis
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
		imprime += str(rg+1) + ' '
	print imprime

	for j in range(Nrings):
		if extconect[current][j] == 1 and j != before:
			before = current
			current = j
			break


