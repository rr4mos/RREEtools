for dir in $(find . -name \*calc )
do
	echo $dir
	cd $dir 
	name=`echo "$dir" | cut -d'.' -f2 | cut -d'/' -f2`  
	
	echo $name
	babel *.msi -o gzmat  $name.gzmat
	cat ../head.com > $name.com

	awk 'NR > 3' $name.gzmat >> $name.com
	
	cd ..	
done
