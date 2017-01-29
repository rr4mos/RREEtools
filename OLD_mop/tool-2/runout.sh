root=`pwd`
toolsdir=/home/rramos/WORK-III/tools

for dir in $(find . -name allmods)
do
cd $dir 
bash $toolsdir/RUNanalisaOrbs.sh 142 20 4 241
cd $root
done

