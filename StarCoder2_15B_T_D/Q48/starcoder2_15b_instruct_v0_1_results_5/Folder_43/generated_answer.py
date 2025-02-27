def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[28]
    tup_set = set(tup[11:28])
    sum_of_integers = sum(range(a + 1, b))
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]