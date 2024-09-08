import os

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHECK CLIB by Feancios Lionet
#
# Verify the validity of +CLIB.seek
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

lib_label0 = "Lib_"
lib_label1 = "Lib_Cmp"
lib_label2 = "Lib_End"
lib_label3 = "Lib_Pos"

# Load +LEQU.s
# ~~~~~~~~~~~~

console_output("Loading LEqu.s...", 2)

input_file_lequ = open("+LEqu.s", "r")
    
file_length_lequ = get_file_length(input_file_lequ)
    
file_content_lequ = input_file_lequ.read()
    
input_file_lequ.close()

lequ_pos_start=0
lequ_pos_end=file_length_lequ

# Load +CLIB.s
# ~~~~~~~~~~~~

console_output("Loading +CLib.s...", 2)

input_file_clib = open("+LEqu.s", "r")
    
file_length_clib = get_file_length(input_file_clib)
    
file_content_clib = input_file_clib.read()
    
input_file_clib.close()

clib_pos_start=0
clib_pos_end=file_length_clib

while True:
    current_line_end = file_content_clib.find("\n", clib_pos_start, clib_pos_end)
        
    if current_line_end == -1:
        console_output("Bad library!", 2)
        exit() 

    current_label_position = file_content_clib.find("Lib_Ini", clib_pos_start, clib_pos_end)

    if current_line_end > -1:
        break
            
    clib_pos_start += current_line_end
    
clib_pos_start=current_label_position+1

while True:
    current_line_end = file_content_clib.find("\n", clib_pos_start, clib_pos_end)

    if current_line_end > -1:
        break

    if ord(file_content[current_search_start]) <= 32:
        current_label_position = file_content_clib.find(lib_label0, clib_pos_start, clib_pos_end)
        
        if current_label_position > -1:
            current_label_position = file_content_clib.find(lib_label1, clib_pos_start, clib_pos_end)
        
            if current_label_position > -1:
                a=""
                
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

                a="L_"+a+":"
                
                label_position = file_content_lequ.find(a, lequ_pos_start, lequ_pos_end)
                
                if label_position == -1:
                    label_position = file_content_clib.find("\n", clib_pos_start, clib_pos_start + 99)
                    
                    if current_label > -1:
                        console_output("Label problem: "+file_content_clib[clib_pos_start:label_position], 2)   
                    else:
                        console_output("Label problem: "+file_content_clib[clib_pos_start:clib_pos_start + 99], 2)
                    
                else:
                    lequ_pos_start=label_position+1
                
            else:
                current_label_position = file_content_clib.find(lib_label2, clib_pos_start, clib_pos_end)

                if current_label_position > -1:
                    break

                current_label_position = file_content_clib.find(lib_label3, clib_pos_start, clib_pos_end)
                    
                if current_label_position > -1:
                
                    label_position = file_content_clib.find("\n", clib_pos_start, clib_pos_start + 99)
                    
                    if current_label > -1:
                        console_output("LIB_DEF still prsemt: "+file_content_clib[clib_pos_start:label_position], 2)   
                    else:
                        console_output("LIB_DEF still prsemt: "+file_content_clib[clib_pos_start:clib_pos_start + 99], 2)
    
    clib_pos_start=current_line_end+1

console_output("Completed!", 2)