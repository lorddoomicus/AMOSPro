#!/bin/bash
#
# As of 2024-09-02 does not yet work.  Hopefully some point in the future
#
# (c) 2024 Derrik Walker v2.0
# This is licensed for use under the MIT License
#
#
# 2024-09-07	dwalker		Initial Version

echo "This is experimental and does not yet work.  Do not use it!"
exit 0

cd ../dist/AMOS
bdir=$( dirname `pwd` )

vamos -V bdir:$bdir --cwd bdir:AMOS -- APSystem/APCmp bdir:c/Check_CLib.AMOS TYPE=0 WB NOERR NODEF
vamos -V bdir:$bdir --cwd bdir:AMOS -- APSystem/APCmp bdir:c/Get_Chunk.AMOS TYPE=0 WB NOERR NODEF
vamos -V bdir:$bdir --cwd bdir:AMOS -- APSystem/APCmp bdir:c/Library_Digest.AMOS TYPE=0 WB NOERR NODEF
vamos -V bdir:$bdir --cwd bdir:AMOS -- APSystem/APCmp bdir:c/Make_Labels.AMOS TYPE=0 WB NOERR NODEF
vamos -V bdir:$bdir --cwd bdir:AMOS -- APSystem/APCmp bdir:c/Make_Toktable.AMOS TYPE=0 WB NOERR NODEF
