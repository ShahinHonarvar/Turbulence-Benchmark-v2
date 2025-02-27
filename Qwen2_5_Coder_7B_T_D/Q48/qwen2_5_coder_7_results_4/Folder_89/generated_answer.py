def return_binary_or_hexa(tup):
    a = tup[55]
    b = tup[84]
    total = 0
    for i in range(a + 1, b):
        if i not in tup:
            total += i
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]