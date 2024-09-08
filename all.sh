#!/bin/bash
#
# Builds AMOSPro and creates a lha file that can be copied to an Amiga to be installed
#
# Sometime in the future, this should probably be replaced with a Makefile
#
# (c) 2024 Derrik Walker v2.0
# This is licensed for use under the MIT License
#
# 2024-09-07	dwalker		Initial Version

# Fail if any part fails
set -e 

# Target dir tree for build
AMOS=dist/AMOS

# check that the necessary tools are installed
if ! which lha > /dev/null 2>&1 
then 
	echo lha does not appear to be installed and in your path
	echo Please install it 
	exit 1
fi

if ! which vasmm68k_mot > /dev/null 2>&1 
then 
	echo vasm for m68k_mot does not appear to be installed and in your path
	echo Please install it
	exit 1
fi

echo "*** Building RELEASE build ***"
./amospro.sh
./extensions.sh
./compiler.sh
./cleanup.sh build

echo
echo "*** Success RELEASE build ***"

if [ "$comptests" == "YES" ]
then
	echo Adding compiler tests

	echo Coming soon
fi

echo
echo "*** Making LHA archive to transfer to Amiga ***"
lha -c AMOSPro.lha dist 
