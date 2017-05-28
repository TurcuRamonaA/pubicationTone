for D in [0-9]*-*;
do 
	cd $D
	for f in *.gz; do 
   	 name=$(basename "${f}" .gz)
  	 zcat "${f}" > "${name}"
	done
	rm -rf *.gz
	rm -rf __COMPLETED__
	cd ..
	
done

