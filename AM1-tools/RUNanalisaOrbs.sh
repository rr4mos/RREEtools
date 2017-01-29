
#uso: RUNanalisaOrbs.sh num.atms no.de.aneis no.de.orbitais.analisados homo.level

echo "AM1-tools -- RR / 2013 e 2014 / V.update 2015."


tools=/home/rramos/Dropbox/RREE-tools/AM1-tools/

#retirado para trabalho já com pdb feito (em 2015)

#Gera pdb educado via babel com CONECT
#for arq in $(ls mopac-*.arc)
#do 
#	echo $arq
#	python $tools/arc2mop.py $arq $1
#done 


#Gera topologia do backbone
for arq in $(ls mopac-*.out.pdb)
do 
	python $tools/gettopo.py $arq > $arq-RINGS
	
done

#Analisa os orbitais
for arq in $(ls mopac-*.out)
do 
	echo "gerando os psi^2..."
	python $tools/analisaorbitais.py $arq $1 $4 $3> $arq-ORBITAIS

	echo "analisando extensao..."
	python $tools/extende.py $arq-ORBITAIS $2 $3 > $arq-EXTENSAO
	echo "extende:: analisa ateh: HOMO -`expr $3 - 1`"

done

	grep 'vetone:' *EXTENSAO | awk '{print $2}' > .evec
	grep 'energy:' *EXTENSAO | awk '{print $2}' > .eval
	paste .eval .evec > patch-eigen.dat


