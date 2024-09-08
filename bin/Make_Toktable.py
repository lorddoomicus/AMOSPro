import os

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAKE TOKTABLE by Francois Lionet
# Converted to Python 3 by Rolf Missing 11.07.2024
#   Validated by binary comparison of output file 
#   against original output file.
#
# Creation of the intermediate test table
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def is_eof(file):
    current_position = file.tell()    
    file.seek(0, os.SEEK_END)
    end_position = file.tell()    
    file.seek(current_position, os.SEEK_SET)
    return current_position == end_position

def console_output(output_string, line_end_option):
    if line_end_option == 1:
        output_string+=chr(0xd)
    
    if line_end_option == 2:
        output_string+=chr(0xa)

    print(output_string)



console_output("Making Token Table", 2)
console_output("", 2)

# Load up the token list

# Open file "+Lib.s"

input_file = open("+Lib.s", "r")

# Open file "+Toktab_Verif.Bin"

output_file = open("+Toktab_Verif.Bin", "wb")

# Parse input file amd generate output file

while True:

    end_file_processing = False
    
    # Look for "TOKEN_START"
    
    while True:
        try: 
        
            input_line = input_file.readline()
        
            if is_eof(input_file):
                console_output("End of file found", 2)
                end_file_processing = True
                break
                
            if input_line.find("TOKEN_START") > -1:
                console_output("TOKEN_START found", 2)
                break            
        
        except:
            console_output("Exception in reading line", 2)
            end_file_processing = True
            break
            
    if end_file_processing == True:
        break
        
    while True:
        
        # Look for "TOKEN_END"
        
        try: 
        
            input_line = input_file.readline()
            
            console_output(input_line, 2)
            
            if is_eof(input_file):
                console_output("End of file found", 2)
                end_file_processing = True
                break
                
            if input_line.find("TOKEN_END") > -1:
                console_output("TOKEN_END found", 2)
                break     

        except:
            console_output("Exception in reading line", 2)
            end_file_processing = True
            break
        
        # Look for "//" on current line
        # [Any text]
        # [Any text]                 			//$2F$03$05$00

        encode_position = input_line.find("//") 
        
        input_line_uppercase = input_line.upper()

        console_output(input_line, 2)

        if encode_position > -1:
        
            # Get token and write out as bytes
        
            encoded = input_line[encode_position+2:]
            
            decoded_a = encoded[1:3]
            decoded_b = encoded[4:6]
            decoded_c = encoded[7:9]
            decoded_d = encoded[10:12]

            output_file.write(bytes.fromhex(decoded_a+decoded_b+decoded_c+decoded_d))

    if end_file_processing == True:
        break

    
# Close input file
    
input_file.close()

# Close output file

output_file.close()
    
console_output("Completed!", 2)