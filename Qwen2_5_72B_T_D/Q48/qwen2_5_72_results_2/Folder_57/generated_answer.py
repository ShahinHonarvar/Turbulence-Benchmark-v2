def return_binary_or_hexa(tup):
    a = tup[25]
    b = tup[80]
    sum_missing = sum(range(a + 1, b)) - sum(tup[26:80])
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]