def return_binary_or_hexa(tup):
    a = tup[16]
    b = tup[87]
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in tup[a + 1:b]]
    if not missing:
        return ''
    total -= sum(missing)
    if total % 2 == 0:
        return format(total, 'x')
    else:
        return format(total, 'b')