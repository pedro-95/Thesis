Time = $( date +'%y.%m.%d %H:%M:%S' )
push:
	echo "The time is: $Time"
	git add .
	git commit -m m
	git push -u origin main
