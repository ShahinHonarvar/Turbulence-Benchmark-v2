def return_binary_or_hexa(tup):
    a = tup[19]
    b = tup[32]
    missing = set(range(a + 1, b)) - set(tup[a + 1:b])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()