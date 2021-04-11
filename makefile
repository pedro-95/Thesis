m = `date +'%y.%m.%d %H:%M:%S'`
push:
	: "$m"
	git add .
	git commit -m "$m"
	git push -u origin main
