def return_binary_or_hexa(tup):
    a = tup[40]
    b = tup[200]
    sum_missing = sum(set(range(a + 1, b)) - set(tup[41:200]))
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]