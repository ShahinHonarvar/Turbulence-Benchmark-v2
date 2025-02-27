def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[90]
    missing_sum = sum(range(a + 1, b)) - sum(tup[a + 1:b])
    return format(missing_sum, 'b') if missing_sum % 2 else format(missing_sum, 'x')