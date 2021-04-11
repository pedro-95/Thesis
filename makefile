m = $(date +'%y.%m.%d %H:%M:%S')
push:
	echo $m
	git add .
	git commit -m m
	git push -u origin main
