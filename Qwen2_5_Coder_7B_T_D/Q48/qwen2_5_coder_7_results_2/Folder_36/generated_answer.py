def return_binary_or_hexa(tup):
    a = tup[110]
    b = tup[348]
    total_sum = sum(range(a + 1, b))
    missing_integers = [x for x in range(a + 1, b) if x not in tup[tup.index(a) + 1:tup.index(b)]]
    if sum(missing_integers) % 2 == 0:
        return hex(sum(missing_integers))[2:]
    else:
        return bin(sum(missing_integers))[2:]