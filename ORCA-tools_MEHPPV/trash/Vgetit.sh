#compila dados e chama analise de conectividade

tools=/home/rramos/Dropbox/RREE-tools/GAU-tools

echo "running Vgetit"

echo > .ac
echo > .ss

for name in $(ls -1 *-VEXTENSAO)
do

grep 'vetone:' $name | awk '{ s = ""; for (i = 2; i <= 21; i++) s = s $i " "; print s }'  > .vo
grep 'LxE'     $name | awk '{ s = ""; for (i = 2; i <=  3; i++) s = s $i " "; print s }'  > .le
grep 'orb:'     $name | awk '{ s = ""; for (i = 2; i <=  3; i++) s = s $i " "; print s }'  > .oi

#rotulando em detalhe

nn=`wc -l .vo | awk '{print $1}'` 
echo $name > .fix
rm -f .nm
for i in `seq 1 $nn` 
do
sed 's/-VEXTENSAO//g' .fix >> .nm
done

paste .nm .oi .le .vo  >> .ac
paste .nm .oi .le .vo  >> .ss

#echo '' >> .ac

echo "running... conexo.py"
python $tools/conexo.py

done
