
## Welcome to an unofficial AMOS Professional source code repository.

### This one is for building on Linux or macOS. 


This is a version of the AMOS Pro repo that has all the necessary scripts to build AMOS Pro with Linux or macOS, or any UNIX like OS I suppose. It has had all the extraneous stuff removed and only has what is needed for making an installable AMOS Professional distribution.

## Buidling AMOS Pro

### Tools Needed

There are several tools needed to build AMOS.

**Vasm**

Vasm is the assembler, and therefore has to be installed.  
Download the latest source from here: http://sun.hasenbraten.de/vasm/index.php?view=relsrc

To build the code, you need a working C compiler as well. gcc, clang, or any ANSI C compiler will work. After downloading and untaring the source for vasm, run the following

```
make CPU=m68k SYNTAX=mot
cp vasmm68k_mot $HOME/bin # or other location in your path
```

Usage as needed to build the AMOS source

```
vasmm68k_mot
   -devpac    Devpac-compatibility mode - required for source compatibility. 
   -Fhunkexe  Generate executable file 
   -nocase    Ignore case in names for symbols etc. Some need, some don’t it seems
   -w         Hide all warning messages 
   -o <output file>      
   <input file>
```

Example:

`vasmm68k_mot -devpac -w -Fhunkexe -o Installer/AMOS_Pro/APSystem/AMOSPro.Lib +lib.s`

NOTE: Some files require -nocase and some do not.   This will be seen in the build scripts

**Python Scripts**

There are AMOS apps needed for building that have been converted to Python and were obtained from  the following: 

https://github.com/makeandbreak/AMOS-Professional-Tooling/blob/main/AMOS%20Professional%202.0%20Windows%20compile%20tools%2020240723.zip

I’ve included them in repo for convenience. They can be found in the bin directory.

**LHA**

Lha has to be installed. For Mac, it can be installed from homebrew.  Most Linux distros should have it in their repos. 


### Build Process

**Source files.**

The source files are all *+<file>.s*  

**NOTE:** To edit a source file with vi, you have to specify a double dash, -- in the command like:

```vi -- +lib.s```

**Directory Structure**

```
AMOSPro 		All the main source files are here as well as build scripts
├── dist	 	Distribution directory where all the built files go
├── bin 		Support files and scripts
├── compiler 		Compiler source files
├── comptests		Compiler test programs
├── extensions		Extension support files 
└── includes		Include files
```

The dist tree layout is pretty much the same after an install from floppies and is self explanatory:

```
dist					
└── AMOS			
    ├── APSystem	
    ├── Accessories	
    ├── Compiler	
    ├── Examples	
    ├── Productivity1	
    ├── Productivity2	
    └── Tutorial		
```

After running the build scripts, you’ll have an LHA file, AMOSPro.lha,  that will contain the contents of the dist directory for installing on an Amiga. There is an AmigaDos script called InstallAMOS in the dist directory that will install it on an amiga.  There is also a .info file for the AMOS folder.

**Build Scripts**

There are 4 build and one cleanup Bash scripts.  They probably should be replaced by makefiles at some point. But for now, these work.

This calls the other three build scripts and the clean up script to clean up temp files from the build
all.sh 

This one builds the main environment 

`amospro.sh`

This one builds the extensions.

`extensions.sh`

This one builds the compiler.

`compiler.sh`

Cleanup script can be used to clean up after a build.

`cleanup.sh` 
 
To build everything, run the **all.sh** script.  

The **all.sh** script will:

1. Verify that all the required tools are installed
2. Run the three individual build scripts
3. Run cleanup.sh build to clean up temporary build files
4. Make the LHA file to copy to an Amiga

Each of the 3 individual scripts can be run by themselves, but have to be run in order or you may get errors.  The cleanup script is optional in that case. Also note that there is no tool checking in the individual scripts, which could lead to errors if vasm is not installed correctly. 

**cleanup.sh**

cleanup.sh has 4 options:

- all - cleans up everything
- Build - cleans up the temporary files left after a build
- dist - cleans up the dist directory for a clean build
- logs - cleans up the log files left after a build

**Installing**

After bulding, copy AMOSPro.lha to your Amiga, or use in Emulator. Uncompress it, and run the InstallAMOS DOS script to install it.  You may have to set the dest varible in the installer script with where you want it installed.  It will make an AMOS directory in that dest. 

```
lha x AMOSPro.lha
cd dist
execute InstallAMOS
```

### Changes need for build

Several Source changes were needed to get it to build with AMOS:

1. +B.s Line 549 bne. changed to bne.s
2. +Edit.s line 14475 cmp.s changed to cmp.b
3. compiler/+CompExt.s lines 1544 and 1555 MOVE.B changed to MOVE.W
4. compiler/+APComp.s line 11063 bne. changed to bne.s
5. compiler/+Header.s lines 1184 and 1195 MOVE.B changed to MOVE.W
6. compiler/+CLib.s line 810 cmp.s changed to cmp.b
7. bin/Library_Digest.py lines 286 and 298 changed slashes for UNIX style
8. Numerous changes to deal with Linux using a case sensitive filesystem. 

### Building AMOS on Other Platforms

Generally, building on other platforms are out of scope, but here are a couple details.

**Amiga**

Get source from the official release:  https://github.com/AOZ-Studio/AMOS-Professional-Official

And copy to Amiga or Emulator running 2.10 or higher. 

Unless you have a fresh install from Floppies or other place,  you’ll need to copy amos.library from AMOS/APSystem to libs:

In the source, just execute the aall script to start the build

'execute aall'

On a real amiga, it will take several minutes to complete.

**Issues**

On I ran into was when compiling compiler/aclib, it sometimes fails on the c/Check_Clib command, yet when ran by hand it works fine.

**Windows**

More information can be found here:

This Youtube video: 

https://www.youtube.com/watch?v=LOhXxYsfggQ&list=PL8YJ6-4X9NNWxuwIEsueskw9QowvG4Tun&index=1

For tooling see:

https://github.com/makeandbreak/AMOS-Professional-Tooling


### Special Thanks

There were a few people who made this effort possible.

First off, thanks to François Lionet for creating the original project. 

His official repo can be found at: https://github.com/AOZ-Studio/AMOS-Professional-Official

Next special thanks to Pietro Ghizzoni for releasing AMOS to the public domain. 

And finally, very special thanks to The Tech Rabbit for figuring some of this stuff out and providing python scripts.

Tech Rabbit can be found:

https://www.youtube.com/@TheTechRabbit \
https://github.com/makeandbreak
