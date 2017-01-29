

BLOCO DENSITY OF STATES
=======================
*COMPILA ENERGIAS DO ESPECTRO 
getallspectra.sh --> compila dados do espectro todo buscando pelos diretorios allmods (padrao de armazenamento)
	getspectra.py

*ANALISA DADOS (DISPERSAO DO ESPECTRO)
	dispersao.py  --> para fazer os graficos de linhas com dispersao (var***)


BLOCO ORBITAIS
==============
* GERA ANALISE DE ORBITAIS (ENERGIAS E PSI^2 POR ANEL)
RUNanalisaOrbs.sh  --> roda dentro do diretorio com os arquivos .out (mopac)
	arc2mop.py
	gettopo.py
	analisaorbitais.py -> $ARQ-ORBITAIS
	extende.py         -> $ARQ-EXTENSAO
* GERA ANALISE DE EXTENSAO DOS ORBITAIS X ENERGIA

getcomparis.sh 
    run getit.sh (pega todos $ARQ-EXTENSAO e gera arqivos   
              ocultos .ac .ss .fc)

    pega todos .ac .ss .fc -> allcuts.dat, fcallcuts.dat, 
                              allconexos.dat

    conexo.py (pega arquivos ocultos e gera arquivo conexos.dat filtrando tamanho x energia apenas para estados conexos)

---
para rodar geral o bloco de orbitais ea analise de extensao

runout.sh
getcomparis.sh  
(atualmente /home/rramos/WORK-III/050-inst/PDB ) 




