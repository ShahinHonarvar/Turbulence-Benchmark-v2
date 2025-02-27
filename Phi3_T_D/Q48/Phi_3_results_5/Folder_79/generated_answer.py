def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[7]
    missing_sum = sum((x for x in range(a + 1, b) if x not in tup[1:7]))
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')