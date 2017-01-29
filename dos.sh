grep '# energy:' *ORBITAIS | awk '{print $7, $3 }' > espectro.dat

