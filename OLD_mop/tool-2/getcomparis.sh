root=`pwd`
tools=/home/rramos/WORK-III/tools

rm allcuts.dat
rm fcallcuts.dat
rm allconexos.dat

for dir in $(find . -name allmods | sort)
do 

cd $dir
now=`pwd`
echo $now
echo "# $now" >> $root/allcuts.dat
echo "# $now" >> $root/fcallcuts.dat

bash $tools/getit.sh 

cat .ss     >> $root/allcuts.dat
echo ''     >> $root/allcuts.dat

cat .fc     >> $root/fcallcuts.dat
echo ''     >> $root/fcallcuts.dat

cat conexos.dat >> $root/allconexos.dat

cd $root
done

