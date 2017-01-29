def minusarc(string):
	stok = ''
	for i in range(len(string)-1):		
#		print string[i]
		if string[i] == '.' and string[i+1] == 'a':
			break
		stok += string[i]
	return stok

import sys 
from os import system

filename = sys.argv[1]
Nat = int(sys.argv[2])

system('echo "XXXX" > .moptemp ')
system('echo "XXXX" >> .moptemp ')
system('tail -n '+str(Nat+2)+' '+filename +'>> .moptemp')

nameok = minusarc(filename)+'.out.pdb'
print nameok
system('babel -imopin .moptemp -opdb ' + nameok)
