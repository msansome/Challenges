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


def make_binary(bits, num):
        digits = ''
        for i in range (bits-1, -1, -1):
                digits = digits + str(num // (2 ** i))
                num = num % (2 ** i)
        return digits

def make_hex_digit(nibble):
    hex_digits="0123456789ABCDEF"
    hex_d = 0
    for i in range(0,4):
        hex_d += int(nibble[i]) * 2**(3-i)
    hex_d = hex_digits[hex_d]
    return hex_d

def make_hex_number(bits, bin_num):
    hex_num = ''
    if bits % 8 != 0:                        # If we need to:
        byte_length = bits + (8 - (bits % 8))# Round up the bits to nearest multiple of 8
        bin_num = bin_num.zfill(byte_length) # Pad with zeros
    else:
        byte_length = bits
    for nibble in range (0, byte_length, 4):
        hexD = bin_num[nibble:nibble+4] # Slice the binary into chunks of 4
        hex_num += make_hex_digit(hexD) # Build the Hex number a nibble at a time
    return hex_num

def hex2dec(hexno):
    hex_digits="0123456789ABCDEF"
    total = 0
    hexno = hexno[::-1] # reverse the hexadecimal string 
    for n in range(len(hexno)):
        total += (hex_digits.index(hexno[n]) * 16**n) # for each hex digit value
                                                      # multiply by 16 ^ n
    return total


############################
# Main program starts here #
############################

no_of_bits = 16 # Here you can set the bit-length 
maxno = (2**no_of_bits)-1


num = input(f'Please enter a number between 1 and {maxno}: ')
while not num.isdigit() or int(num) > maxno:
	num = input(f'Please enter a number between 1 and {(2**no_of_bits)-1}: ')
num = int(num)

binary_num = make_binary(no_of_bits, num)
hex_num = make_hex_number(no_of_bits, binary_num)


print(f'{num} is {binary_num} in binary and {hex_num} in hexadecimal.')
print(f'{hex_num} is {hex2dec(hex_num)} in decimal')

