'''
Possible answer to Q15 on the OCR 20 Coding Challenges
Calculate notes / coins to give as bin_number
'''


dec_number = 7

def make_bin_number(dec_number):
    bin_number = []
    for i in range(7,-1,-1):
        bin_number.append(int(dec_number // 2**i))
        print("i is",i, "2**i is", 2**i, "dec_number is",dec_number,"bin_number is" ,dec_number // 2**i),
        dec_number = round(dec_number % 2**i)
        #print(dec_number)
    return bin_number

bin_number = make_bin_number(dec_number)
print(dec_number,"is", "".join(str(bin_number)),"in binary.")

    

