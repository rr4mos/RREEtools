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
done

#Analisa os orbitais
for arq in $(ls *.com) 
do 
	name=`echo "$arq" | cut -d'.' -f1`

	echo "gerando os psi^2... Orbitais virtuais."
#	python $tools/Orbitais-AM1_GAU.py $name $1 $3 $4 > $name-ORBITAIS
#	python $tools/Orbitais-HF_GAU.py $name $1 $3 $4 > $name-ORBITAIS
	python $tools/OrbitaisVirtuais-HF_GAU.py $name $1 $3 $4 > $name-VORBITAIS

	echo "analisando extensao... Orbitais virtuais."
	echo "	python $tools/extende.py $name-VORBITAIS $2 $4 > $name-VEXTENSAO"
	python $tools/extendeFULL.py $name $name-VORBITAIS $2 $4 > $name-VEXTENSAO
	echo "extende:: analisa ateh: HOMO -$4"

done
	rm matrix.mat
	rm .conect
	bash $tools/getcomparis.sh V

