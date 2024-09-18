#!/bin/bash


temp=$1

if [ $temp -gt 55 ]
then 
	if [ $temp -lt 67 ]
	then
		echo "COLD"
	elif [ $temp -lt 85 ]
	then
		echo "NICE"
	else
		echo "HOT"
	fi
else
	echo "FREEZING"
fi
