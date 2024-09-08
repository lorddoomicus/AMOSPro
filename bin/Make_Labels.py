import os

from datetime import datetime

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAKE LABELS by Francois Lionet
# Converted to Python 3 by Rolf Missing 12.07.2024
#   Validated by comparison of output files 
#   against original output files.
#
# Create a table of labels for AMOSPro 2.0
# L_xxxx    equ $000
# Make the table of internal routines of AMOSPro 
# from the library.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
                output_file_name3, output_file_title3,
                lib_label0, lib_label1, lib_label2,
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

    if output_file_name3 != "":
        output_file3 = open(output_file_name3, "w")
        
        output_file3.write("; ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+chr(10))
        output_file3.write("; "+output_file_title3+" on the "+date_stamp+" "+time_stamp+chr(10))  
        output_file3.write(";"+chr(10))
        output_file3.write("; ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+chr(10))

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
            
        current_label_position = file_content.find(lib_label0, current_search_start, current_line_end)    

        if current_label_position != -1:
                
            a = ""
            b1 = ""
            b2 = ""
            
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

                if current_label_position == -1:
                    current_label_position = file_content.find(lib_label2, current_search_start, current_line_end)    

                    i = current_label_position
                
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
                        
                    if i > 0:
                        b1 = "\t" + "dc.w" + "\t"+"L_" + a
                        b2 = "\t" + "dc.l" + "\t" + a

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
 
                    if b1 != "":
                        if output_file_name2 != "":
                            output_file2.write(b1 + "\n")
                            output_file2.write(b2 + "\n")                            
       
       
        current_search_start = current_line_end + 1 
        
    if output_file_name2 != "":
        output_file2.write(chr(9)+"dc.w"+chr(9)+"0"+chr(10))    
        output_file2.write(chr(9)+"dc.l"+chr(9)+"0"+chr(10))    
        
    output_file3.write("Lib_Size"+"\t"+"\t"+"equ"+"\t "+str(label_number)+"\n")        
            
    console_output('{: >78}'.format(""), 1)             
    console_output("Number of labels:"+str(label_number), 2)
                          
    if output_file_name1 != "":                      
        output_file1.close()
    
    if output_file_name2 != "":
        output_file2.close()
    
    if output_file_name3 != "":
        output_file3.close()
        
    return date_stamp, time_stamp, label_number, label_value 


console_output("Making Labels Table", 2)
console_output("", 2)

lib_label0 = "Lib_"
lib_label1 = "Lib_Def"
lib_label2 = "Lib_Int"
lib_label3 = "Lib_Empty"
lib_label4 = "Lib_Ext"
lib_label5 = "Lib_Par"
lib_label_set1 = "Lib_Pos"
lib_label_set2 = "Lib_Ini"

# Create the labels for ILIB.S

input_file_name = "+ILib.s"

output_file_name1 = "+LEqu.s"
output_file_title1 = "AMOSPro Internal Library functions"
output_file1_uppend_only = False

output_file_name2 = "+Internal_Jumps.s"
output_file_title2 = "AMOSPro Internal Jump list"

output_file_name3 = "+ILib_Size.s"
output_file_title3 = "AMOSPro Internal Library Size"

output_file_name4 = "+ILib_Functions.s"
output_file_title4 = "AMOSPro Internal Library Definition"

date_stamp = ""
time_stamp = ""

label_number = 0
label_value = 0

date_stamp, time_stamp, label_number, label_value = search_file(input_file_name,
                                                                output_file_name1, output_file_title1, output_file1_uppend_only,
                                                                output_file_name2, output_file_title2,
                                                                output_file_name3, output_file_title3,
                                                                lib_label0, lib_label1, lib_label2,
                                                                lib_label3, lib_label4, lib_label5,
                                                                lib_label_set1, lib_label_set2,
                                                                date_stamp, time_stamp,
                                                                label_number, label_value)

output_file4 = open(output_file_name4, "w")

output_file4.write("; ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+chr(10))
output_file4.write("; "+output_file_title4+" on the "+date_stamp+" "+time_stamp+chr(10))  
output_file4.write(";"+chr(10))
output_file4.write("; ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+chr(10))
output_file4.write("\t"+"Lib_Ini"+"\t"+" 0"+chr(10))
output_file4.write("\t"+"Lib_Pos"+"\t"+str(label_value)+chr(10))

output_file4.close()

# Manufacture the labels of LIB.S
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

output_file1 = open(output_file_name1, "a")

output_file1.write("; Main library"+chr(10))
output_file1.write("; ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+chr(10))

output_file1.close()

input_file_name = "+Lib.s"

output_file_name1 = "+LEqu.s"
output_file1_uppend_only = True

output_file_name2 = ""

output_file_name3 = "+Lib_Size.s"
output_file_title3 = "AMOSPro Main Library Size"

output_file_name4 = ""

search_file(input_file_name,
            output_file_name1, output_file_title1, output_file1_uppend_only,
            output_file_name2, output_file_title2,
            output_file_name3, output_file_title3,
            lib_label0, lib_label1, lib_label2,
            lib_label3, lib_label4, lib_label5,
            lib_label_set1, lib_label_set2,
            date_stamp, time_stamp,
            label_number, label_value)

console_output("Completed!", 2)







 