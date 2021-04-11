#!/bin/bash
T = $( date +'%y.%m.%d %H:%M:%S' )
echo "The time is: $T"
push:
	echo "The time is: $T"
	git add .
	git commit -m m
	git push -u origin main
