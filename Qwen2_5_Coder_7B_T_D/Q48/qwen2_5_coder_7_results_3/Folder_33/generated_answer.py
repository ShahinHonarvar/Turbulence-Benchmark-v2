def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[35]
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in tup[a + 1:b - 1]]
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()