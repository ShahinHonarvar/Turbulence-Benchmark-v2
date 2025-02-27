def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[4])
    sum_of_integers = sum(range(a + 1, b))
    sum_of_integers_in_range = sum((i for i in range(a + 1, b) if i not in tup))
    if sum_of_integers_in_range % 2 == 1:
        return bin(sum_of_integers_in_range)[2:]
    else:
        return hex(sum_of_integers_in_range)[2:].upper()