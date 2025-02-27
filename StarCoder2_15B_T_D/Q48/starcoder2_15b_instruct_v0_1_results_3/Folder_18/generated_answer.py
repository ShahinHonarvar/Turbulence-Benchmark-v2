def return_binary_or_hexa(tup, a, b):
    present_integers = set(tup[a + 1:b])
    sum_of_integers = sum((i for i in range(a + 1, b) if i not in present_integers))
    return bin(sum_of_integers)[2:] if sum_of_integers % 2 else hex(sum_of_integers)[2:]