def return_binary_or_hexa(tup):
    a = tup[3]
    b = tup[9]
    total = sum(range(a + 1, b)) - sum((x for x in tup if a + 1 <= x < b))
    if total % 2 == 0:
        return format(total, 'x')
    else:
        return format(total, 'b')