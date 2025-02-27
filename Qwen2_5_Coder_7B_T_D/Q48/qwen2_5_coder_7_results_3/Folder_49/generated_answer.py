def return_binary_or_hexa(tup):
    a = tup[80]
    b = tup[200]
    total_sum = sum(range(a + 1, b))
    missing_integers = set(range(a + 1, b)) - set(tup[80:201])
    if sum(missing_integers) % 2 == 1:
        return bin(sum(missing_integers))[2:]
    else:
        return hex(sum(missing_integers))[2:].upper()