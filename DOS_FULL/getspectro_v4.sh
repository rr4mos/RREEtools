# getspectro_v3.sh ESTADO_MAIS_ALTO
# recolhe o espectro geral (s/ restricao a estados conexos)

echo '#orbitais // RR' > espectro.dat
echo '#orbitais // RR' > Mergeespectro.dat
echo '#orbitais // RR' > Merge_idxE.dat

for i in `seq 0 $1`
do 
echo $i
echo '#orbitais // RR' > homo-$i
done

for file in $(ls -1 ../../*/allpatches.dat | sort )
do
	echo $file
	echo '' >> espectro.dat
	echo '# ' $file >> espectro.dat
	while read line; do
#	echo  $line
	orbind=`echo $line  | awk '{print $3}'`
#	echo $orbind
	if [ -n "$orbind" ]; then
#	echo $orbind
	if [ $orbind -le $1 ]; then
#		echo $line	
		echo $line | awk '{print  $3, $4, $5 }' >>      espectro.dat
		echo $line | awk '{print  $3, $4, $5 }' >> Mergeespectro.dat
		echo $line | awk '{print  $4, $5 }' >> homo-$orbind
			
	fi
	fi
	done < $file
done


echo '#orbitais conexos// RR' > conex.espectro.dat
echo '#orbitais conexos// RR' > conex.Mergeespectro.dat
for file in $(ls -1 ../../*/allconexos.dat | sort )
do
	echo $file
	echo '' >> conex.espectro.dat
	echo '# ' $file >> conex.espectro.dat
	while read line; do
#	echo  $line
	orbind=`echo $line  | awk '{print $3}'`
#	echo $orbind
	if [ -n "$orbind" ]; then
#	echo $orbind
	if [ $orbind -le $1 ]; then
#		echo $line
		echo $line | awk '{print $4, $5 }' >>      conex.espectro.dat
		echo $line | awk '{print $4, $5 }' >> conex.Mergeespectro.dat
	fi
	fi
	done < $file
done



