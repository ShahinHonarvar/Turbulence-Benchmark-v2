def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[85]
    total = sum(range(a + 1, b)) - sum((tup[i] for i in range(37, 85)))
    if total % 2 == 0:
        return format(total, 'x')
    else:
        return bin(total)[2:]