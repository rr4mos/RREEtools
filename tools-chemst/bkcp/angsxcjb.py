from os import system
import sys

ensid = sys.argv[1]
DBdir= '/home/rramos/WORK-III/MOD6/nvt-mod6/NVTDYN/P3HT/'

def getid(string):
	i = 2
	clean =''
#	print string
	while string[i] != '.':
		clean = clean+ string[i]
		i+=1
#	print clean
	return clean
	
system('find . -name allmods | sort  > .dirs')

dirs = file('.dirs','r').readlines()


for dir in dirs:

	chainid   = int(getid(dir.split()[0]))
	
	eearqname = dir.split()[0]+'/conexos-2.dat'
	eearq     = file(eearqname,'r').readlines()

# pegando os vetores de morfologia
	Fens = file( DBdir+ensid+'/angs.intra.1nb.dat', 'r').readlines()
	i = 0
	for i in range(len(Fens)):
		Fcid = Fens[i].split()[0]
		if int(Fcid) == chainid:
			k = i
			chainT = []
			chainOP = []
			chainIP = []
			while k < 30:
				#print Fens[k]
				chainT.append(Fens[k].split()[2])
				chainOP.append(Fens[k].split()[3])
				chainIP.append(Fens[k].split()[4])
				k+=1
			break
			
		i+=1
	print '#Ts:',chainT
	print '#OP:',chainOP
	print '#IP:',chainIP

	EEf = file(eearqname,'r').readlines()
	for any in EEf:
		cjr = int(any.split()[1])
		cjL = int(any.split()[2])
		cjbR=cjr+cjL
		cjbL=cjr
		print '#',any.split()[3]
		if cjbL > 0:
			if cjbL != 1:
				if any.split()[3][cjbL-2]!= 'X':
					print cjbL,chainT[cjbL-1],chainOP[cjbL-1],chainIP[cjbL-1]
				else: 
					print '#filtro X > '

#		print cjbL, cjbR	
		if cjbR < 31:
			if any.split()[3][cjbR-1]!= 'X':
				print cjbR,chainT[cjbR-1],chainOP[cjbR-1],chainIP[cjbR-1]
			else:
				print '#filtro < X'

	exit()

