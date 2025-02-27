def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[51]
    tup_set = set(tup[20:52])
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in tup_set:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()