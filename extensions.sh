#!/bin/bash
#
# Builds AMOS Extensions
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

echo *** Assembling the extensnions ****

echo
echo *** Assembling AMOSPro_Music.Lib ***
python bin/Library_Digest.py extensions/+Music.s > amusic_Library_Digest.log
vasmm68k_mot -devpac -nocase -w -Fhunkexe -o ${AMOS}/APSystem/AMOSPro_Music.Lib extensions/+Music.s

echo
echo *** Assembling AMOSPro_Compact.Lib ***
python bin/Library_Digest.py extensions/+Compact.s > acompact_Library_Digest.log
vasmm68k_mot -devpac -nocase -w -Fhunkexe -o ${AMOS}/APSystem/AMOSPro_Compact.Lib extensions/+Compact.s

echo
echo *** Assembling AMOSPro_Request.Lib ***
python bin/Library_Digest.py extensions/+Request.s > arequest_Library_Digest.log
vasmm68k_mot -devpac -nocase -w -Fhunkexe -o ${AMOS}/APSystem/AMOSPro_Request.Lib extensions/+Request.s

echo
echo *** Assembling AMOSPro_IOPorts.Lib ***
python bin/Library_Digest.py extensions/+IO_Ports.s > aio_Library_Digest.log
vasmm68k_mot -devpac -w -Fhunkexe -o ${AMOS}/APSystem/AMOSPro_IOPorts.Lib extensions/+IO_Ports.s
