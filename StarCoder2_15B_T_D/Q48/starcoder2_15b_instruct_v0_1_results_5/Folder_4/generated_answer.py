def return_binary_or_hexa(t):
    a = t[49]
    b = t[74]
    present_integers = set(t[49:75])
    sum_of_missing_integers = sum((i for i in range(a + 1, b) if i not in present_integers))
    if sum_of_missing_integers % 2 == 1:
        return bin(sum_of_missing_integers)[2:]
    else:
        return hex(sum_of_missing_integers)[2:]