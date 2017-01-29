work=`pwd`
for dir in $(find . -name allmods)
do
	echo $dir
	cd $dir
	cp ../../../run0.sh .
	bash ./run0.sh
	cd $work
done

