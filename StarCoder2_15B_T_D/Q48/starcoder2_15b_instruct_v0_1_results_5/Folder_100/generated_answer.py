def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[78]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_of_integers += i
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:].lstrip('0')
    else:
        return bin(sum_of_integers)[2:].lstrip('0')