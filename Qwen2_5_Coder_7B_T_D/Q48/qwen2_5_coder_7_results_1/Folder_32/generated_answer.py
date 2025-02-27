def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[90]
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[86:91]))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')