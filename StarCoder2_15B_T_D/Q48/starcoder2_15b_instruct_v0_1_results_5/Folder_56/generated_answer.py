def return_binary_or_hexa(tup):
    a = tup.index(7)
    b = tup.index(9)
    missing = []
    for i in range(a + 1, b):
        if i not in tup:
            missing.append(i)
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()