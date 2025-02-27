def return_binary_or_hexa(tup):
    a, b = (tup[46], tup[91])
    sum_of_integers = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in tup:
            sum_of_integers -= i
    if sum_of_integers & 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()