def return_binary_or_hexa(tup):
    a = tup[62]
    b = tup[96]
    total = 0
    for i in range(a + 1, b):
        if i not in tup:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()