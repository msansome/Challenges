'''
Possible answer to Q15 on the OCR 20 Coding Challenges
Convert a decimal number into binary - and Hex
'''


def make_bin_number(dec_number):
    bin_number = ""
    # Empty string to hold output
    for i in range(7,-1,-1):
        # Cycle through 8 bits
        bin_number += str((dec_number // 2**i))
        # Work out the integer division of 2**i and append it to the answer string
        dec_number = round(dec_number % 2**i)
        # Work out the remainder
    return bin_number

def make_hex_digit(nibble):
    hex_digits="0123456789ABCDEF"
    hex_d = 0
    for i in range(0,4):
        hex_d += int(nibble[i]) * 2**(3-i)
    hex_d = hex_digits[hex_d]
    return hex_d
    

def make_hex_number(bin_num):    
    if len(bin_num) < 8:
        pad = 8 - len(bin_num)
        pad_str = "0"*pad
        bin_num = pad_str+bin_num
    part_1 = bin_num[:4]
    part_2 = bin_num[4:]
    hex_1 = make_hex_digit(part_1)
    hex_2 = make_hex_digit(part_2)
    hex_num = hex_1 + hex_2
    return hex_num


# Main Program starts here

dec_number = int(input("Please enter a number (between 0 and 255) to be converted into binary: "))
bin_number = make_bin_number(dec_number)
hex_number = (make_hex_number(bin_number))
print(dec_number,"is", bin_number,"in binary.")
print(bin_number,"is",hex_number,"in hexadecimal")

    
