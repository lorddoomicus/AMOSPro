import os
import sys
import argparse

from pathlib import Path
from datetime import datetime

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LIBRARY DIGEST by Francois Lionet
# 
# This program analyse your source code, counts all the
# labels and creates a file called "Source_Size.s"
# Include this file at the start of your extension.
# It also creates a label list called "Source_Labels.s"
# where all the labels are listed.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_file_length(file):
    current_position = file.tell()    
    file.seek(0, os.SEEK_END)
    end_position = file.tell()    
    file.seek(current_position, os.SEEK_SET)
    return end_position

def console_output(output_string, line_end_option):
    if line_end_option == 1:
        output_string+=chr(0xd)
    
    if line_end_option == 2:
        output_string+=chr(0xa)

    print(output_string)
    
# Routine search
def search_file(file_name, 
                output_file_name1, output_file_title1, output_file1_uppend_only,
                output_file_name2, output_file_title2,
                lib_label0, lib_label1,
                lib_label3, lib_label4, lib_label5,
                lib_label_set1,lib_label_set2,
                date_stamp, time_stamp,
                label_number, label_value):

    console_output("Loading "+file_name+"...", 2)
    
    # Load the file
    
    input_file = open(file_name, "r")
    
    file_length = get_file_length(input_file)
    
    file_content = input_file.read()
    
    input_file.close()

    # We can ignore these as we do not need memory 
    # bank reservations in Python.
    #   Reserve As Work [bank_number], [length]
    #   Sload [file_number] To Start([bank_number]), [length]
    #   ADOLD=Start(10) : ADEND=Start(10)+Length(10)
    
    # _DATE$ : D$=Param$ : _TIME$ : T$=Param$
    # Example of D$ 08-07-2024 
    # Example of T$ 21:31:17
    # So we use same format
    
    # current date and time
    
    now = datetime.now() 

    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")

    date_stamp = day + "-" + month + "-" + year

    time_stamp = now.strftime("%H:%M:%S")
    
    # Open the shipping files
    
    if output_file_name1 != "":
    
        if output_file1_uppend_only == False: 
            output_file1 = open(output_file_name1, "w")
        
            output_file1.write("; ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+chr(10))
            output_file1.write("; "+output_file_title1+" on the "+date_stamp+" "+time_stamp+chr(10))  
            output_file1.write(";"+chr(10))
            output_file1.write("; ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+chr(10))
        else:
            output_file1 = open(output_file_name1, "a")
                    
    if output_file_name2 != "":
        output_file2 = open(output_file_name2, "w")
        
        output_file2.write("; ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+chr(10))
        output_file2.write("; "+output_file_title2+" on the "+date_stamp+" "+time_stamp+chr(10))  
        output_file2.write(";"+chr(10))
        output_file2.write("; ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+chr(10))

    current_search_start = 0
    
    # Is fixed value
    
    current_search_end = file_length   

    while True:
        
        # Hunt
        #  function: find a string of characters in memory
        #  first=Hunt(start To finish,s$)
        
        current_line_end = file_content.find("\n", current_search_start, current_search_end)
        
        if current_line_end == -1:
            break 
            
        if ord(file_content[current_search_start]) <= 32:
                
            a = ""
            
            current_label_position = file_content.find(lib_label_set1, current_search_start, current_line_end)    

            if current_label_position == -1:
                current_label_position = file_content.find(lib_label_set2, current_search_start, current_line_end)    

            if current_label_position != -1:
                
                a = ""
                
                for label_position in range(current_label_position, current_line_end+1):
                    c = file_content[label_position]
                    
                    if c <= " ":
                        break
                        
                for label_position in range(label_position, current_line_end+1):
                    c = file_content[label_position]
                    
                    if c > " ":
                        break
                
                for label_position in range(label_position, current_line_end+1):
                    c = file_content[label_position]
                    
                    if c <= " ":
                        break
                        
                    a += c
                
                label_value = int(a)
                
                label_number = label_value
                
                a = ""
                
            else:
        
                i = 0
                
                current_label_position = file_content.find(lib_label1, current_search_start, current_line_end)    
    
                if current_label_position == -1:
                    current_label_position = file_content.find(lib_label4, current_search_start, current_line_end)    
                   
                if current_label_position == -1:
                    current_label_position = file_content.find(lib_label5, current_search_start, current_line_end)    
                
                if current_label_position != -1:
                                
                    a = ""
                     
                    for label_position in range(current_label_position, current_line_end+1):
                        c = file_content[label_position]
                        
                        if c <= " ":
                            break

                    for label_position in range(label_position, current_line_end+1):
                        c = file_content[label_position]
                        
                        if c > " ":
                            break
                            
                    for label_position in range(label_position, current_line_end+1):
                        c = file_content[label_position]
                        
                        if c <= " ":
                            break
                            
                        a += c
                        
                    a = "L_" + a + ":"
                    
                    if len(a) < 8:
                        a = a + "\t" + "\t" + "\t"
                    elif len(a) < 16:
                        a = a + "\t" + "\t"
                    elif len(a) < 24:
                        a = a + "\t"
                        
                    a = a + "set" + chr(9) + str(label_value) 

                    label_value +=1
                    
                    label_number +=1
                    
                else:
 
                    current_label_position = file_content.find(lib_label3, current_search_start, current_line_end)    

                    if current_label_position > -1:
                        label_value +=1
                    
                        label_number +=1
                                            
                if a != "":
                    output_file1.write(a + "\n")
                
                    if (label_number and 15) == 0:
                        console_output('{: >30}'.format(""), 1)             
                        console_output("Computing label" + str(label_value), 1)
       
       
        current_search_start = current_line_end + 1 
        
    output_file2.write("Lib_Size"+"\t"+"\t"+"equ"+"\t "+str(label_number)+"\n")        
            
    console_output('{: >78}'.format(""), 1)             
    console_output("Number of labels:"+str(label_number), 2)
                          
    if output_file_name1 != "":                      
        output_file1.close()
    
    if output_file_name2 != "":
        output_file2.close()
        
    return date_stamp, time_stamp, label_number, label_value 


console_output("AMOSPro II Library digest by Francois Lionet", 2)
console_output("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", 2)
console_output("Public domain, written using AMOS Professional.", 2)
console_output("", 2)
 
# Check command line argument

parser = argparse.ArgumentParser("Library_Digest.py")
parser.add_argument("source_file", help="Source file (.s file) to analyze.", type=str)

args = parser.parse_args()

# Extract parameter
# ~~~~~~~~~~~~~~~~~

source_file_path = Path(args.source_file)

if not source_file_path.is_file():
    console_output("Can not access '"+args.source_file+"'",2)
    exit()
    
# Compute the names of the files
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
source_file_folder_and_name = args.source_file    

source_file_folder = source_file_path.parent.name
 
source_file_name = source_file_path.name

source_file_name_no_extension = source_file_path.stem

# Search   
# ~~~~~~

# Input file

input_file_name = source_file_folder_and_name

# Output Labels

if source_file_folder=="":
    output_file_name1 = source_file_name_no_extension+"_Labels.s"
else:
    # output_file_name1 = source_file_folder+"\\"+source_file_name_no_extension+"_Labels.s" ==> 2024-08-24 No Dos slashes please
    output_file_name1 = source_file_folder+"/"+source_file_name_no_extension+"_Labels.s" 

output_file1_uppend_only = False

output_file_title1 = input_file_name+", list of the library functions"

# Output Size

if source_file_folder=="":
    output_file_name2 = source_file_name_no_extension+"_Size.s"
else:
    # output_file_name2 = source_file_folder+"\\"+source_file_name_no_extension+"_Size.s"  ==> 2024-08-24 No Dos slashes please
    output_file_name2 = source_file_folder+"/"+source_file_name_no_extension+"_Size.s"

output_file_title2 = input_file_name+", library size"

# Search

lib_label0 = "Lib_"
lib_label1 = "Lib_Def"
lib_label3 = "Lib_Empty"
lib_label4 = "Lib_Ext"
lib_label5 = "Lib_Par"
lib_label_set1 = "Lib_Pos"
lib_label_set2 = "Lib_Ini"

date_stamp = ""
time_stamp = ""

label_number = 0
label_value = 0

search_file(input_file_name,
            output_file_name1, output_file_title1, output_file1_uppend_only,
            output_file_name2, output_file_title2,
            lib_label0, lib_label1, 
            lib_label3, lib_label4, lib_label5,
            lib_label_set1, lib_label_set2,
            date_stamp, time_stamp,
            label_number, label_value)

console_output("Completed!", 2)
