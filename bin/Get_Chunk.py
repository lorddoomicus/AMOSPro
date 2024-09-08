import os
import sys
import argparse

from pathlib import Path

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GET CHUNK by Bruce Uncle, Implemented by Marc Williams 
# with code from Francois Lionet and Michael D. Cox
# Converted to Python 3 by Rolf Missing 19.07.2024
#   Validated by comparison of output files 
#   against original output files.
# 
# This program extracts the chunk needed for the .config file
# from the assembled object .o file.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def console_output(output_string, line_end_option):
    if line_end_option == 1:
        output_string+=chr(0xd)
    
    if line_end_option == 2:
        output_string+=chr(0xa)

    print(output_string)
    
def get_file_length(file):
    current_position = file.tell()    
    file.seek(0, os.SEEK_END)
    end_position = file.tell()    
    file.seek(current_position, os.SEEK_SET)
    return end_position

console_output("AMOSPro II Get Chunk by Amos Factory Team",2)
console_output("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",2)
console_output("Public domain, written using AMOS Professional",2)
console_output("",2)

# Check command line arguments

parser = argparse.ArgumentParser("Get_Chunk.py")
parser.add_argument("object_file", help="Assembled object (.o file) to extract from.", type=str)
parser.add_argument("config_file", help="Destination (.config) configuration file.", type=str)

args = parser.parse_args()

# Load the file
# ~~~~~~~~~~~~~

object_file = Path(args.object_file)

if not object_file.is_file():
    console_output("Can not access '"+args.object_file+"'",2)
    exit()
    
console_output("Loading '"+args.object_file+"'...",2)

input_file = open(object_file, "rb")
    
file_length = get_file_length(input_file)
   
file_content = input_file.read()
    
input_file.close()

# Save the file
# ~~~~~~~~~~~~~

output_file = open(args.config_file, "wb")

console_output("Saving '"+args.config_file+"'...",2)

# Size of data block to transfer encoded as Big-endian (Motorola) long word

block_size_encoded = [file_content[28], file_content[29], file_content[30], file_content[31]]

byte_array = bytearray(block_size_encoded)

block_size = int(byte_array[::].hex(), 16)

# Data blcok to transfer starts at offset 32 and has size of block_size
# Each block to transfer is 4 bytes

output_file.write(file_content[32:32+block_size*4])

output_file.close()
        
console_output("Completed!", 2)

