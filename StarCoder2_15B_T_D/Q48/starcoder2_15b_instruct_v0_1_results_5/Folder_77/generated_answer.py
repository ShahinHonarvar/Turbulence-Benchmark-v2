import math
import binascii

def return_binary_or_hexa(tup):
    a = tup[18]
    b = tup[52]
    sum_of_integers = sum(range(a + 1, b))
    for i in range(18, 52):
        if tup[i] not in range(a + 1, b):
            sum_of_integers -= tup[i]
    if sum_of_integers % 2 == 1:
        binary_representation = binascii.bin(sum_of_integers)[2:]
        return format(int(binary_representation, 2), 'b')
    else:
        hexadecimal_representation = binascii.hex(sum_of_integers)[2:]
        return format(int(hexadecimal_representation, 16), 'x').upper()