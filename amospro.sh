#!/bin/bash
#
# Builds the main AMOS App and Libaries 
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

echo *** Assembling RELEASE build ***

echo
echo *** Making Token Table +Toktab_Verif.Bin ***
python bin/Make_Toktable.py > alib_MakeToktable.log

echo *** Making Label Files ***
python bin/Make_Labels.py > alib_Make_Labels.log

echo *** Assembling AMOSPro.Lib ***
vasmm68k_mot -devpac -w -Fhunkexe -o ${AMOS}/APSystem/AMOSPro.Lib +Lib.s

echo
echo *** Assembling AMOS.library ***
vasmm68k_mot -devpac -nocase -w -Fhunkexe -o ${AMOS}/APSystem/AMOS.library +W.s

echo
echo *** Assembling AMOSPro ***
vasmm68k_mot -devpac -nocase -w -Fhunkexe -o ${AMOS}/AMOSPro +B.s

echo
echo *** Assembling the Editor Configuration ***
vasmm68k_mot -devpac -nocase -w -Fhunkexe -o Editor_Config.o +Editor_Config.s
python bin/Get_Chunk.py Editor_Config.o ${AMOS}/Tutorial/Extra_Configs/Editor_Config.Backup > adata_Get_Chunk.log

echo *** Assembling the default Interpreter Configuration ***
vasmm68k_mot -devpac -nocase -w -Fhunkexe -o Interpreter_Config.o +Interpreter_Config.s
python bin/Get_Chunk.py Interpreter_Config.o ${AMOS}/Tutorial/Extra_Configs/Interpreter_Config.Backup > adata_Get_Chunk.log

echo *** Installing default configuration ***
cp ${AMOS}/Tutorial/Extra_Configs/Editor_Config.Backup ${AMOS}/APSystem/AMOSPro_Editor_Config
cp ${AMOS}/Tutorial/Extra_Configs/Interpreter_Config.Backup ${AMOS}/AMOSPro_Interpreter_Config

echo
echo *** Assembling AMOSPro_Editor ***
vasmm68k_mot -devpac -nocase -w -Fhunkexe -o ${AMOS}/APSystem/AMOSPro_Editor +Edit.s

echo
echo *** Assembling AMOSPro_Monitor ***
vasmm68k_mot -devpac -nocase -w -Fhunkexe -o ${AMOS}/APSystem/AMOSPro_Monitor +Monitor.s

