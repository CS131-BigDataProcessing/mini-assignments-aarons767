#!/bin/bash


curr_date=$(date)

echo "--ACTIVITY ONE--"
echo "The time and date are: $curr_date"

echo "Let's see who is logged into the system:" $(who)

echo -e "\nFor $USER, the home directory is $HOME"


echo "--ACTIVITY TWO--"
name=$1
amount=$2
echo "My name is $name and I have $amount in my wallet"

echo "--ACTIVITY THREE--"

mathvar1=$((1+5))
mathvar2=$((mathvar1*20))
mathvar3=10
mathvar4=$((mathvar1*$((mathvar2+mathvar3))))
echo "Variable 1 is $mathvar1. Variable 2 is $mathvar2. Using $mathvar3 for Variable 3, our final Variable 4 is $mathvar4."

echo "--ACTIVITY 4--"
variable=$(echo "scale=3; 4.5/1.7" | bc)
echo "Our floating variable is $variable"

