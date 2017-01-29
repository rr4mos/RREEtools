rm .ac
rm .ss
rm .fc

tools=/home/rramos/WORK-III/tools

for name in $(ls -1 *-EXTENSAO)
do

grep 'vetone:' $name | awk '{ s = ""; for (i = 2; i <= 21; i++) s = s $i " "; print s }'  > .vo
grep 'LxE'     $name | awk '{ s = ""; for (i = 2; i <=  3; i++) s = s $i " "; print s }'  > .le
grep 'vetflt:' $name | awk '{ s = ""; for (i = 2; i <= 21; i++) s = s $i " "; print s }'  > .vf

nn=`wc -l .vo | awk '{print $1}'` 
echo $name > .fix
rm -f .nm
for i in `seq 1 $nn` 
do
sed 's/mopac-opt//g' .fix | sed 's/.msi.out-EXTENSAO//g' >> .nm
done

paste .le .vo >> .ac
paste .nm .le .vo >> .ss
paste .nm .le .vf >> .fc

echo '' >> .ac
echo '' >> .ss
echo '' >> .fc

python $tools/conexo.py

done
