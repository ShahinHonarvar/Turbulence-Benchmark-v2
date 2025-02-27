def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[36]
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[20:36]))
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')