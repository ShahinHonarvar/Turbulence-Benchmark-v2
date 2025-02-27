def return_binary_or_hexa(tup):
    a = tup[50]
    b = tup[92]
    missing_ints = set(range(a + 1, b)) - set(tup[a + 1:b])
    sum_missing_ints = sum(missing_ints)
    if sum_missing_ints % 2 == 0:
        return hex(sum_missing_ints)[2:]
    else:
        return bin(sum_missing_ints)[2:]