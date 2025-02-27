def return_binary_or_hexa(t, a, b):
    sum_of_integers = sum((i for i in range(a + 1, b) if i not in t))
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]