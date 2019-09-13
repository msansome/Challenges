'''Decimal to Binary converter using recursion'''

def dec2bin(dec_num):
    if dec_num > 1:
        dec2bin(dec_num // 2)
    print(dec_num % 2, end='')
    bin_no.append(str(dec_num % 2))


# Main program starts here


bin_no = []
dec_num = 12

dec2bin(dec_num)
print(bin_no)
bin_str = "".join(bin_no)
print(bin_str)
