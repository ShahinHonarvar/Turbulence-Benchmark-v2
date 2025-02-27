def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[10])
    full_range = set(range(a + 1, b))
    present_in_tup = set(tup[a + 1:b])
    missing = full_range - present_in_tup
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()