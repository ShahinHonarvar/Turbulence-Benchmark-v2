def return_binary_or_hexa(tup: tuple) -> str:
    a = tup[55]
    b = tup[84]
    sum_of_integers = sum(range(a + 1, b))
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()