tools=/home/rramos/Dropbox/RREE-tools/GAU-tools


for arq in $(ls *.com)
do 
	name=`echo "$arq" | cut -d'.' -f1`
	echo "name: $name"
	echo 'running babel...'	
	babel -igzmat $name.com -opdb  $name.pdb
	echo 'running gettopo...'
	python $tools/gettopoFIXED.py $name.pdb $1 $2 > $name-RINGS
	python $tools/geralists.py $name
	python $tools/../CheckAtDist.py $name.pdb $1 $2 

done



