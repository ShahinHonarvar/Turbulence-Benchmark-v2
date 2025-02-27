def return_binary_or_hexa(tup):
    a = tup[72]
    b = tup[93]
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in tup[72:94]]
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    else:
        return bin(sum_missing)[2:]