def return_binary_or_hexa(tup):
    a = tup[56]
    b = tup[88]
    total = sum(range(a + 1, b))
    missing = [x for x in range(a + 1, b) if x not in tup[a + 1:b]]
    if missing == list(range(a + 1, b)):
        return ''
    total -= sum(missing)
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]