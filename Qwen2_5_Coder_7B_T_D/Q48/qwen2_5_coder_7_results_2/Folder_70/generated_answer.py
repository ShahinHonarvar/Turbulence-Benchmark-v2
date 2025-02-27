def return_binary_or_hexa(tup):
    a = tup[43]
    b = tup[70]
    total = sum(range(a + 1, b)) - sum((tup[i] for i in range(44, 70)))
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]