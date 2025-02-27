def return_binary_or_hexa(tup):
    a = tup[45]
    b = tup[48]
    total = sum(range(a + 1, b)) - sum((i for i in range(a + 1, b) if i in tup[45:48]))
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]