arq = file('patch-eigen.dat','r').readlines()

ee=[]
ev=[]
for line in arq:
	ee.append( line.split()[0] )
	ev.append( line.split()[1] )
#print ee
#print ev
conexo = []
naocon = []
fstv = []
lenv = []
for i in range(len(ev)):
	string = ev[i]
	j  = 0
	cn = 1
	while j < len(string):
		if string[j] == '1':
			L = 0
			k = j
			fst = j
			while string[k] == '1':
#				print string[k]
				L+=1
				k+=1
				if k == len(string):
					break
			# se encontrar mais um 1 nao eh conexo (tem buraco)
			while k < len(string):
				if string[k] == '1':
					cn = 0

				k+=1
			j = k
		j+=1
	if cn == 1:
		print 'eh con.',L, string		
		conexo.append(i)
		fstv.append(fst+1)
		lenv.append(L)
		print fst+1,L
	else:
#		print 'nao eh.', string
		naocon.append(i)

#print 'conexos:', len(conexo),conexo
#print 'naocone:',len(naocon),naocon

confile = file('conexos.dat','w')
k=0
for i in conexo:
	confile.write( ee[i]+' '+str(fstv[k]).rjust(2)+' '+str(lenv[k]).rjust(2)+' '+ev[i]+'\n')
	k+=1
confile.close()


