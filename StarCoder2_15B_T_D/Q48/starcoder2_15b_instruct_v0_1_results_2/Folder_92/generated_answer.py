def return_binary_or_hexa(x):
    a, b = (x[0], x[2])
    integers_in_range = set(range(a + 1, b))
    sum_of_integers = sum(integers_in_range - set(x[1:3]))
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()