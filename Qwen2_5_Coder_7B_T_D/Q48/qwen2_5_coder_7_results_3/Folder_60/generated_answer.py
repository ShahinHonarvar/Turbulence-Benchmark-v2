def return_binary_or_hexa(tup):
    a = tup[38]
    b = tup[52]
    total = sum(range(a + 1, b)) - sum((tup[i] for i in range(38, 53)))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()