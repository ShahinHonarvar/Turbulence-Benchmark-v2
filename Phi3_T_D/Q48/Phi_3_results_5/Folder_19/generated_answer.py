def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[4]
    existing = set(tup[1:5])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing))
    if missing_sum % 2:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')