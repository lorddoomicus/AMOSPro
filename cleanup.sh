#!/bin/bash
#
# Cleans up the files after builds and for clean builds  
#
# (c) 2024 Derrik Walker v2.0
# This is licensed for use under the MIT License
#
# 2024-09-07    dwalker         Initial Version

# Fail if any part fails
set -e 

# Target dir tree for build
AMOS=dist/AMOS

# List of files to clean up
declare -a dist
declare -a build
declare -a comptest
declare -a all

declare -a files

usage="Usage: $0 [all|build|dist|comptest|logs] ( all is default )"

if [ "$#" -ge 2 ]
then
	echo $usage
	exit 1
fi

if [ "$#" -eq 1 ]
then
	clean=$1
fi

if [ "$#" -eq 0 ]
then
	clean="all"
fi

if [ "$clean" = "help" ]
then
	echo $usage
	exit 0
fi

if [ "$clean" != "all" -a "$clean" != "build" -a "$clean" != "dist" -a "$clean" != "logs" ]
then
	echo $clean is not valid
	echo $usage
	exit 1
fi

echo "*** Cleaning up $clean files ***"

build=(
	"+ILib_Functions.s"
	"+ILib_Size.s"
	"+Lib_Size.s"
	"+Internal_Jumps.s"
	"extensions/+Music_Labels.s"
	"extensions/+Music_Size.s"
	"extensions/+Compact_Labels.s"
	"extensions/+Compact_Size.s"
	"extensions/+Request_Labels.s"
	"extensions/+Request_Size.s"
	"extensions/+IO_Ports_Labels.s"
	"extensions/+IO_Ports_Size.s"
	"compiler/+CLib_Labels.s"
	"compiler/+CLib_Size.s"
	"compiler/+CompExt_Labels.s"
	"compiler/+CompExt_Size.s"
	"+LEqu.s"
	"+Toktab_Verif.Bin"
	"Editor_Config.o"
	"Interpreter_Config.o"
	"Compiler_Config.o"
)

dist=(
	"${AMOS}/APSystem/AMOSPro.Lib"
	"${AMOS}/APSystem/AMOS.library"
	"${AMOS}/AMOSPro"
	"${AMOS}/APSystem/AMOSPro_Editor_Config"
	"${AMOS}/AMOSPro_Interpreter_Config"
	"${AMOS}/APSystem/AMOSPro_Editor"
	"${AMOS}/APSystem/AMOSPro_Monitor"
	"${AMOS}/APSystem/AMOSPro_Compact.Lib"
	"${AMOS}/APSystem/AMOSPro_Music.Lib"
	"${AMOS}/APSystem/AMOSPro_Request.Lib"
	"${AMOS}/APSystem/AMOSPro_IOPorts.Lib"
	"${AMOS}/Tutorial/Extra_Configs/Compiler_Config.Backup"
	"${AMOS}/AMOSPro_Compiler_Config"
	"${AMOS}/APSystem/APCmp"
	"${AMOS}/APSystem/Compiler.Lib"
	"${AMOS}/APSystem/AMOSPro_Compiler.Lib"
	"${AMOS}/APSystem/Header_CLI.Lib"
	"${AMOS}/APSystem/Header_Backstart.Lib"
	"AMOSPro.lha"
)

if [ "$clean" = "build" ] 
then
	files=("${build[@]}")

elif [ "$clean" = "dist" ]
then
	files=("${dist[@]}")

elif [ "$clean" = "all" ]
then
	files=("${build[@]}")
	files+=("${dist[@]}")
fi 

for file in "${files[@]}"
do
	echo -n "$file ... "
	if [ -e "$file" ]
	then
		rm $file
		echo Deleted.
 	else
 	 	echo Does not exist.
	fi
done

if [ "$clean" = "logs" -o "$clean" = "all" ]
then
	echo "Deleting log files ... "
	rm -v *.log
fi
