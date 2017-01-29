#uso: RUNanalisaOrbs.sh num.atms no.de.aneis no.total.de.orbitais no.de.orbitais.analisados 

# $1 = num.atms 
# $2 = no.de.aneis 
# $3 = no.total.de.orbitais 
# $4 = no.de.orbitais.analisados 

tools=/home/rramos/Dropbox/RREE-tools/GAU-tools

#Gera topologia do backbone
for arq in $(ls *.com)
do 
	name=`echo "$arq" | cut -d'.' -f1`
	echo "name: $name"
	echo 'running babel...'	
	babel -igzmat $name.com -opdb  $name.pdb
	echo 'running gettopo...'
	python $tools/gettopoFIXED.py $name.pdb $1 $2 > $name-RINGS
	exit
done

#Analisa os orbitais
for arq in $(ls *.com) 
do 
	name=`echo "$arq" | cut -d'.' -f1`

	echo "gerando os psi^2..."
#	python $tools/Orbitais-AM1_GAU.py $name $1 $3 $4 > $name-ORBITAIS
	python $tools/Orbitais-HF_GAU.py $name $1 $3 $4 > $name-ORBITAIS

	echo "analisando extensao..."
	echo "	python $tools/extende.py $name-ORBITAIS $2 $4 > $name-EXTENSAO"
	python $tools/extende.py $name $name-ORBITAIS $2 $4 > $name-EXTENSAO
	echo "extende:: analisa ateh: HOMO -$4"
done

	grep 'vetone:' *EXTENSAO | awk '{print $2}' > .evec
	grep 'energy:' *EXTENSAO | awk '{print $2}' > .eval
	paste .eval .evec > patch-eigen.dat


