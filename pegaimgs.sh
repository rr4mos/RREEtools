dest=mod5_all
mkdir ~/$dest

for dir in $(find . -name \*0-inst)
do
echo $dir
mkdir ~/$dest/$dir
cp $dir/*.pdb ~/$dest/$dir

done
