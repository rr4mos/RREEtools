root=`pwd`
toolsdir=/home/rramos/Dropbox/RREE-tools/AM1-tools/

for dir in $(find . -name allmods | sort )
do
cd $dir 
echo "diretorio:: `pwd`"
bash $toolsdir/RUNanalisaOrbs.sh 142 20 $1 241
python $toolsdir/conexosnew.py
mv conexos.dat conexos-$1.dat

cd $root
done

