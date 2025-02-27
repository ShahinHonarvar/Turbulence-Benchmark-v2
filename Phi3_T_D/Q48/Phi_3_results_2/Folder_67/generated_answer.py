def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[67]
    present = set(tup[44 + 1:68])
    missing = sum((i for i in range(a + 1, b) if i not in present))
    if missing == 0:
        return ''
    elif missing % 2 == 0:
        return hex(missing)[2:]
    else:
        return bin(missing)[2:]