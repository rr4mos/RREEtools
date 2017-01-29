%mem=2GB
%chk=tiof.chk
%NProcShared=2
%rwf=w1.rwf, 1900MB, w2.rwf, 1900MB, w3.rwf, 1900MB, w4.rwf, 1900MB
# MaxDisk=9500MB
# RHF/6-31G* scf=direct Pop=Regular

Gaussian test 
6-31G*//6-31G* 30_o3htHF
