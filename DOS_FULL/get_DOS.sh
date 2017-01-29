Zhome=`pwd`

for dir in $(find . -name \?\?\? | sort )
do

	echo $dir
	cd $dir 
	python ../EEstates.py > EE.dat
#	grep '#homo' EE.dat | awk '{print  $2}'

	cd $Zhome
done
