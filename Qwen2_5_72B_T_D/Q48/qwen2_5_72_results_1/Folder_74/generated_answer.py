def return_binary_or_hexa(tup):
    a = tup[69]
    b = tup[97]
    present = set(tup[69:98])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    return format(missing_sum, 'x')