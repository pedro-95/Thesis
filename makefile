#!/bin/bash
m ?= "Last update: $(shell date '+%Y/%m/%d - %H:%M')"
push:
	git add .
	git commit -m $m
	git push -u origin main
