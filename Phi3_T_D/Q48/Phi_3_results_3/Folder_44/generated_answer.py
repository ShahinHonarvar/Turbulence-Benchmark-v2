def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[52]
    total = sum((x for x in range(a + 1, b) if x not in tup[36:53]))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]