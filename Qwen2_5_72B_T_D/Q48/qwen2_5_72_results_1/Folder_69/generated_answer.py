def return_binary_or_hexa(tup):
    a = tup[39]
    b = tup[43]
    sum_missing = sum(set(range(a + 1, b)) - set(tup[40:43]))
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]