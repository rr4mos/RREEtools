#chama analise de conexao e compila dados 

root=`pwd`
tools=/home/rramos/Dropbox/RREE-tools/GAU-tools

echo > $1allpatches.dat
echo > $1allconexos.dat

echo "type of calc : " $1
now=`pwd`
echo $now
#echo "# $now" >> $root/$1allpatches.dat

bash $tools/$1getit.sh 
echo $tools/$1getit.sh 

cat .ss     >> $root/$1allpatches.dat

cat conexos.dat >> $root/$1allconexos.dat

#clean

echo 'clean...'

rm conexos.dat
rm .ac
rm .ss
rm .le
rm .vo
rm .hetatm
rm .nm
rm .fix
rm .oi

cd $root

