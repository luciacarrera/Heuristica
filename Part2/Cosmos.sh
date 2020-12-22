#!/usr/bin/bash
# coding=utf-8

#   Authors: Lucía Carrera & Manya Khanna
#   Version: 3.9
#   Since: 22/12/2020

# ---- Implementation of the Bash Script ----

# Help function that displays if user writes -h Flag
Help()
{
    echo "  Help for executing Cosmos.py"
    echo ""
    echo "       /.Cosmos.sh <argv 1>  <argv 2>"
    echo ""
    echo "  <argv 1> is a file that the input information of the problem"
    echo ""
    echo "  <argv 2> is the heuristic function to use. You can type these words:"
    echo "          - manhattanDistance"
    echo "          - euclidean"
    echo ""
    echo "  Example: /.Cosmos.sh ejemplos/problema1.prob manhattanDistance "
    echo ""
}

# Main function
while getopts ":h" option; do
   case $option in
      h) # display Help
         Help
         exit;;
     \?) # incorrect option
         echo "Error: Invalid option"
         exit;;
   esac
done

# Check syntax of arguments
# Only two Arguments
if [ "$#" -ne 2 ]; 
then
    echo "Error: You must enter two arguments"
    exit
fi
# First argument needs to be a File
if ! [ -f "$1" ];
then
    echo "Error: first argument is not a file"
    exit
fi
# Second argument only can take 2 strings
if [ "$2" != "manhattanDistance" ] && [ "$2" != "euclidean" ];
then
    echo "Error: second argument is not a valid heuristic"
    exit
else
    python Cosmos.py "$1" "$2"
fi