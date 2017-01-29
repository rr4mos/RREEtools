def acerta(i):
	i=str(i)
	while len(i)<3:
		i='0'+i
	return i

for i in range(1,101):
 print 'READ BLOCK "../'+acerta(i)+'/Rc60.dat"'
 print 'BLOCK XY "1:3"'
 print 'HISTOGRAM (S0, MESH(0.25, 25, 100), OFF, OFF)'
 print 'S'+str(i)+'.y = S'+str(i)+'.y/(4*PI*S'+str(i)+'.x^2)'
 print 'KILL G0.S0'

