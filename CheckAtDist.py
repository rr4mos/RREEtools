def getxyz(line):
#	print line.split()
	v =[]
	ct = 0
	for i in range(5,8):

#		print line.split()[i]
#		print i

		if len(line.split()[i]) > 8:
#			print 'esse', line.split()[i]
			j = len(line.split()[i])-1
			st2 = ''
			while line.split()[i][j]!='-':
				st2 +=line.split()[i][j]
				j-=1
			st2 +=line.split()[i][j]
			st2= st2[::-1]
			st1 = ''
			j-=1
			while j >= 0:
				st1+=line.split()[i][j]
				j-=1

			st1= st1[::-1]
			v.append( st1 )
			v.append( st2 )
			ct += 2	
		else: 
			if ct < 3:
				v.append(line.split()[i])
				ct+=1
	print 'fixing pdb file...', v
	return v

def dist(x,y,z,i,j):
	d = sqrt((x[i]-x[j])**2 +\
	    (y[i]-y[j])**2 +\
	    (z[i]-z[j])**2)
	return d

def bond(types,i,j,v_list,a_list):

	#bondtyping do tiofeno
	bondtype=[['-','-'],\
		  ['-','-'],\
		  ['-','=']]

#	print a_list
#	print v_list
	if types[i] != types[j]: return  str(types[i])+bondtype[2][0]+ str(types[j])
	else:
		if i in v_list and j in v_list: return str(types[i])+bondtype[1][1]+str(types[j])

		if i in v_list and j not in v_list or i not in v_list and j in v_list: return str(types[i])+bondtype[2][1]+str(types[j])

		if i in v_list and j in a_list or i in a_list and j in v_list: return str(types[i])+bondtype[1][0]+str(types[j])


		else: return str(types[i])+bondtype[1][0]+str(types[j])

	
def genvec(n):
	vec = []
	for i in range(n):
		vec.append([])
	return vec

from math import sqrt
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

###### >>> generalizar para lista de listas <<<<

alpha_list = file('tipo_0.list','r').readlines()
a_list = []
for i in range(len(alpha_list)):
	if len(alpha_list[i].split()) == 2:
		a_list.append([int(alpha_list[i].split()[0])-1,int(alpha_list[i].split()[1])-1])
	else: a_list.append([int(alpha_list[i].split()[0])-1])

print a_list
a_list = [x for sublist in a_list for x in sublist]


vinil_list= file('tipo_1.list','r').readlines()
v_list =[]
for i in range(len(vinil_list)):
	if len(vinil_list[i].split()) == 2:
		v_list.append([int(vinil_list[i].split()[0])-1,int(vinil_list[i].split()[1])-1])

print v_list
v_list = [x for sublist in v_list for x in sublist]

print a_list
print v_list
######

x=[]
y=[]
z=[]

S = []
for line in arq:
#	print line.split()[1], line.split()[2]
	typ  = line.split()[2]
	atid = int(line.split()[1])-1	
	types[atid] = typ
#	if atid in alpha_list:
#		S.append(atid)

#	print len(line.split())
	if len(line.split()) == 11:
		x.append(float(line.split()[5]))
		y.append(float(line.split()[6]))
		z.append(float(line.split()[7]))
	else:
		v=getxyz(line)
		x.append( float(v[0]) )
		y.append( float(v[1]) )
		z.append( float(v[2]) )

#print x,y,z

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

dfile=file('dists.dat', 'w')

pair = []
matrix = file('matrix.mat', 'w')
for i in range(Nat):
	matrix.write(str(i)+'| ')
	for con in conect[i]:
		matrix.write(str(con)+' ')

		if i<con:
			pair.append([i,con])
			dfile.write( '{:2.2f}'.format(dist(x,y,z,i,con))+' '+\
				bond(types,i,con,v_list,a_list)+' '+\
				'{:3d} {:3d}'.format(i+1,con+1)+'\n')
	matrix.write('\n')
matrix.close()
dfile.close()





