'''
OCR 20 Coding Challenges

20 Binary/Hexidecimal/Decimal
======================

Verion 5 - A more sophisticated version which is not limited to 8 bits (0-255)

Mark Sansome - September 2019

Binary/Hexidecimal/Decimal
Create a program which will convert a given decimal up to 255 into its 8-bit binary equivalent.

Extensions:
1. Extend program to convert the binary number to hexadecimal
2. Create a program to convert from hexadecimal to decimal.
'''


def dec2bin(dec_number):
    bin_number = ""
    while dec_number > 0:
        #print(dec_number)
        if (dec_number // 2) >= 0:
            tmp = str(dec_number % 2)
            bin_number = tmp+bin_number
            dec_number = dec_number // 2                  
    return bin_number

def bin2dec(bin_num):
    total = 0
    size = len(bin_num)-1
    for i in range(size, -1,-1):
        total += int(bin_num[i]) * 2**(size-i)
    return total

def hex2dec(hexno):
    hex_digits="0123456789ABCDEF"
    total = 0
    hexno = hexno[::-1] # reverse the hexadecimal string 
    for n in range(len(hexno)):
        total += (hex_digits.index(hexno[n]) * 16**n) # for each hex digit value
                                                      # multiply by 16 ^ n
    return total

def dec2hex(dec_number):
    hex_digits="0123456789ABCDEF"
    hex_number = ""
    while dec_number > 0:
        if (dec_number // 16) >= 0:
            tmp = hex_digits[dec_number % 16]
            hex_number = tmp+hex_number
            dec_number = dec_number // 16                  
    return hex_number

def make_hex_digit(nibble):
    hex_digits="0123456789ABCDEF"
    dec_d = bin2dec(nibble)
    hex_d = hex_digits[dec_d]
    return hex_d

def bin2hex(bin_num):
    hex_num = ''
    byte_length = len(bin_num)
    if byte_length % 8 != 0:
            byte_length = byte_size(byte_length)
            bin_num = bin_num.zfill(byte_length)
    # This function relies upon the length binary number being a multiple of 8!
    for nibble in range (0, byte_length, 4):
        hexD = bin_num[nibble:nibble+4] # Slice the binary into chunks of 4
        hex_num += make_hex_digit(hexD) # Build the Hex number a nibble at a time
    return hex_num

def byte_size(bits):
    if bits % 8 != 0:                        # If we need to:
        byte_length = bits + (8 - (bits % 8))# Round up the bits to nearest multiple of 8
        #bin_num = bin_num.zfill(byte_length) # Pad with zeros
    else:
        byte_length = bits
    return byte_length




############################
# Main program starts here #
############################

no_of_bits = 14 # Here you can set the bit-length 
maxno = (2**no_of_bits)-1


num = input(f'Please enter a number between 1 and {maxno}: ')
while not num.isdigit() or int(num) > maxno:
	num = input(f'Please enter a number between 1 and {(2**no_of_bits)-1}: ')
num = int(num)

binary_num = dec2bin(num)
hex_num = bin2hex(binary_num)


print(f'{num} is {binary_num} in binary and {hex_num} in hexadecimal.')
print(f'{hex_num} is {hex2dec(hex_num)} in decimal')
print(f'and {num} is {dec2hex(num)} in hexadecimal')
