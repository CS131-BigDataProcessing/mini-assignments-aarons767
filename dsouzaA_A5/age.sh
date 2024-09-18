#!/bin/bash


age=$1

if [ $age -lt 13 ]
then
	echo "User is a CHILD"
elif [ $age -lt 20 ]
then
	echo "User is a TEEN"
elif [ $age -lt 65 ]
then
	echo "User is an ADULT"
else
	echo "User is an ELDERLY"
fi

