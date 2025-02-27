def return_binary_or_hexa(tup):
    a = tup[37]
    b = tup[43]
    missing_integers = set(range(a + 1, b)) - set(tup[37:44])
    sum_missing_integers = sum(missing_integers)
    if sum_missing_integers % 2 == 1:
        output = bin(sum_missing_integers)[2:]
    else:
        output = hex(sum_missing_integers)[2:]
    output = output.lstrip('0')
    if output.startswith('0b'):
        output = output[2:]
    elif output.startswith('0x'):
        output = output[2:]
    return output