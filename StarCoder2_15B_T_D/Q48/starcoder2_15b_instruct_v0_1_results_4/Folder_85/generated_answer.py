def return_binary_or_hexa(t):
    a, b = (t[1], t[8])
    sum_of_integers = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in t:
            sum_of_integers -= i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()