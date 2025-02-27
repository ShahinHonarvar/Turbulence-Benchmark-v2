def return_binary_or_hexa(tup):
    a = tup[2]
    b = tup[7]
    total = sum(range(a + 1, b))
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[3:7]))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')