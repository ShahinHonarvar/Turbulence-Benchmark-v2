def return_binary_or_hexa(tup):
    a = tup[32]
    b = tup[44]
    total = sum(range(a + 1, b))
    missing = set(range(a + 1, b)) - set(tup[a + 1:b])
    if missing:
        total -= sum(missing)
    if total % 2 == 0:
        return format(total, 'x')
    else:
        return format(total, 'b')