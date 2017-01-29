tools=/home/rramos/WORK-III/tools
work=`pwd`

for dir in $(find . -name allmods)
do
	cd $dir
	for arq in $(ls *.out)
	do
		python $tools/getspectra.py $arq
	done
	cd $work
done
