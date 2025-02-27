def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[89]
    full_range = set(range(a + 1, b))
    present = set(tup[87:89])
    missing = full_range - present
    if missing:
        sum_missing = sum(missing)
        if sum_missing % 2 == 1:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:]
    return ''