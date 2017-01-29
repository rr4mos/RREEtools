homed=`pwd`

for dir in $(find . -name \*-inst | sort )
do 
cd $dir
numb=$(echo $dir|cut -c3-5)
echo $numb
python ../angsxcjb.py $numb > axcb.dat
cd ..

done
