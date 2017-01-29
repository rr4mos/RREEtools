#filtro de conexidade sobre os estados

infos = file('.ac', 'r').readlines()
out = file('conexos.dat', 'w')

for line in infos:
	line= line.split()
	if len(line) > 0:
		lineV= line[5]
		ct = 0
		i=0
		isl = []
		print lineV
		while i < len(lineV)-1:
			if lineV[i] == '1':
				j=i+1
				ct = 1
				while lineV[j] == '1':
					ct+=1
					j+=1
					if j == len(lineV):
						break
				i = j
				isl.append(ct)
#				print 'isl', isl
			i+=1
#			print i,line[i]
		print 'seg.c:', len(isl)
		print 'seg.lengths:', isl

#filtrando
		if len(isl) == 1:
			out.write( line[0]   + '     '+ line[1] + ' ' +line[2]\
			    +'         '+ line[3]+ ' '+line[4]\
                            + '        '+ line[5]+'\n')


out.close()
