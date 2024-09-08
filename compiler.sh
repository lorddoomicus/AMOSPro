#!/bin/bash
#
# Builds AMOS compiler, libs, and includes
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

echo *** Assembling the Compiler ****

echo
echo *** Assembling the Compiler Configuration ***
vasmm68k_mot -devpac -nocase -w -Fhunkexe -o Compiler_Config.o compiler/+Compiler_Config.s
python bin/Get_Chunk.py Compiler_Config.o ${AMOS}/Tutorial/Extra_Configs/Compiler_Config.Backup > acdata_Get_Chunk.log

echo *** Installing compiler configuration ***
cp ${AMOS}/Tutorial/Extra_Configs/Compiler_Config.Backup ${AMOS}/AMOSPro_Compiler_Config


echo
echo *** Assembling APCmp Command Line Compiler ***
vasmm68k_mot -devpac -w -Fhunkexe -o ${AMOS}/APSystem/APCmp compiler/+APComp.s

echo
echo *** Assembling Compiler.Lib ***
python bin/Library_Digest.py compiler/+CLib.s > aclib_Library_Digest.log
python bin/Check_CLib.py > aclib_Check_CLib.log

vasmm68k_mot -devpac -w -Fhunkexe -o ${AMOS}/APSystem/Compiler.Lib compiler/+CLib.s

echo
echo *** Assembling AMOSPro_Compiler.Lib ***
python bin/Library_Digest.py compiler/+CompExt.s > acompext_Library_Digest.log
vasmm68k_mot -devpac -w -Fhunkexe -o ${AMOS}/APSystem/AMOSPro_Compiler.Lib compiler/+CompExt.s

echo
echo *** Assembling Header Files ***
vasmm68k_mot -devpac -nocase -w -Fhunkexe -o ${AMOS}/APSystem/Header_CLI.Lib compiler/+Header.s
vasmm68k_mot -devpac -nocase -w -Fhunkexe -o ${AMOS}/APSystem/Header_Backstart.Lib compiler/+Header_Backstart.s
