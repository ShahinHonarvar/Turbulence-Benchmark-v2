def return_binary_or_hexa(t):
    a = t[69]
    b = t[97]
    present = set(t[69:98])
    missing_sum = sum((x for x in range(a + 1, b) if x not in present))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return '{:b}'.format(missing_sum)