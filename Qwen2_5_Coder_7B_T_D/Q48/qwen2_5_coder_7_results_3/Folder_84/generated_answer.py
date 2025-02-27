def return_binary_or_hexa(tup):
    a = tup[32]
    b = tup[44]
    total = sum(range(a + 1, b)) - sum(filter(lambda x: a + 1 <= x <= b - 1, tup))
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]