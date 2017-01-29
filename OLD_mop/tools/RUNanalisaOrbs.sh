
#uso: RUNanalisaOrbs.sh num.atms no.de.aneis no.de.orbitais.analisados homo.level


tools=/home/rramos/WORK-III/tools

#Gera pdb educado via babel com CONECT
for arq in $(ls mopac-*.arc)
do 
	echo $arq
	python $tools/arc2mop.py $arq $1
done 


#Gera topologia do backbone
for arq in $(ls mopac-*.out.pdb)
do 
	python $tools/gettopo.py $arq > $arq-RINGS
	
done

#Analisa os orbitais
for arq in $(ls mopac-*.out)
do 
	echo "gerando os psi^2..."
	python $tools/analisaorbitais.py $arq $1 $4 > $arq-ORBITAIS

	echo "analisando extensao..."
	python $tools/extende.py $arq-ORBITAIS $2 $3 > $arq-EXTENSAO
	echo "extende:: analisa ateh: HOMO -$3"

	grep 'LxE' *EXTENSAO | awk '{print $2, $3}' > LxE.dat
done




