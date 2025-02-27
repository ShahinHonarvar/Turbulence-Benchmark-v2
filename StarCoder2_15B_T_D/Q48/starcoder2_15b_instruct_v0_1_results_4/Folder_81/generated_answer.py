def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[100]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        binary_representation = bin(sum_of_integers)[2:]
        return binary_representation
    else:
        hexadecimal_representation = hex(sum_of_integers)[2:].upper()
        return hexadecimal_representation