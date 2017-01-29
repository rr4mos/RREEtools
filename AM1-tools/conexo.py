

infos = file('.ac', 'r').readlines()
out = file('conexos.dat', 'w')

for line in infos:
	line= line.split()
	if len(line) > 0:
		ct = 0
		i=2
		isl = []
		print line
		while i < len(line)-1:
			if line[i] == '1':
				j=i+1
				ct = 1
				while line[j] == '1':
					ct+=1
					j+=1
					if j == len(line):
						break
				i = j
				isl.append(ct)
#				print 'isl', isl
			i+=1
		print 'seg.c:', len(isl)
		print 'seg.lengths:', isl

#filtrando
		if len(isl) == 1:
			out.write( line[0] + '  '+ line[1] + '\n')


out.close()
