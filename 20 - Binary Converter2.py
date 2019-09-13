'''
Possible answer to Q15 on the OCR 20 Coding Challenges
Convert a decimal number into binary
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

# Main Program starts here

dec_number = int(input("Please enter a number (between 0 and 255) to be converted into binary: "))
bin_number = make_bin_number(dec_number)
print(dec_number,"is", bin_number,"in binary.")

    

