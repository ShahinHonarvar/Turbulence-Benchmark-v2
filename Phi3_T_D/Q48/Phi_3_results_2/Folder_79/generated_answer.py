def return_binary_or_hexa(tup):
    a, *middle, b = tup[1:-1]
    missing_sum = sum(set(range(a + 1, b)) - set(middle))
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    return format(missing_sum, 'x')