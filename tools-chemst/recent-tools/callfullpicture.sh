
mkdir datafullpicture$1 

for a in $(find $1 -name \*pxcb.dat | sort)
do
        aa=`cut -d "/" -f 2 <<< "$a" | cut -c1-3`

	echo $a $aa
	python fullpicture.py $a $aa > datafullpicture$1/data$aa.dat
done

