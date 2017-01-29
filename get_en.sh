grep 'energy' mopac-opt*.msi.out-ORBITAIS | awk '{print $7, $3}' | sort 
