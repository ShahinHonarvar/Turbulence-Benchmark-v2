def return_binary_or_hexa(tup):
    a = tup[3]
    b = tup[8]
    total = sum(range(a + 1, b)) - sum((x for x in tup if a < x < b))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]