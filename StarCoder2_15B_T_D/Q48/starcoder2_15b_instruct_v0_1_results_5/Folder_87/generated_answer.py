def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[43]
    missing = set(range(a + 1, b)) - set(tup[21:43])
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper() if hex(total).startswith('0x') else hex(total)[2:].lower()