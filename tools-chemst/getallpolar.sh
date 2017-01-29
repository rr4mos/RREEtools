rm -f *.dat
cat *-inst/*-pxcb.dat    > WASTEpxcb.dat
gnuplot -e  "set table; set output 'allpxcb.dat' ; plot 'WASTEpxcb.dat' u 2:3"

cat *-inst/*-pxcnonb.dat > WASTEpxcnonb.dat
gnuplot -e  "set table; set output 'allpxcnonb.dat' ; plot 'WASTEpxcnonb.dat' u 2:3"

rm -f WASTE*.dat

echo 'copiando mapas polares para ../analisa/histograma/'

cp *px*.dat ../analisa/histograma/

