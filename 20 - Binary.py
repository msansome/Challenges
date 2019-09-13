bits = 8
maxno = (2**bits)-1


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


num = input(f'Please enter a number between 1 and {maxno}: ')
while not num.isdigit() or int(num) > maxno:
	num = input(f'Please enter a number between 1 and {(2**bits)-1}: ')
num = int(num)

digits = make_binary(bits, num)
nibble1 = digits[:4]
nibble2 = digits[4:]

print(digits)
print(f'{make_hex_digit(nibble1)}{make_hex_digit(nibble2)}')

