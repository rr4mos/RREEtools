import sys
name= sys.argv[1]
rings = file(name+'-RINGS', 'r').readlines()

lists = [0,1,3]
atids = [[],[],[]]
eqtypes =[1,2]


for ring in rings:
	ring =ring.split()

	for id in lists:
		atids[lists.index(id)].append( ring[id] )

for i in range(len(eqtypes)):
	arqout = file('tipo_'+str(i)+'.list','w')
	print 'tipo', i
	
	for j in range(len(atids[i])):
		ptr = ''	
#		print eqtypes[i]
		for k in range(eqtypes[i]):
			ptr+=str('{:5d}'.format(int(atids[i+k][j])))+' '
			
		ptr=ptr+'\n' 		
		arqout.write(ptr)
	
	arqout.close


