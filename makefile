#!/bin/bash
all:
	T = $( date +'%y.%m.%d %H:%M:%S' )
	echo "The time is: $T"
push:
	git add .
	git commit -m m
	git push -u origin main
