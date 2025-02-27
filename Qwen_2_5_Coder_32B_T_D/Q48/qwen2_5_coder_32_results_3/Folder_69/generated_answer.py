def return_binary_or_hexa(t):
    a = t[39]
    b = t[43]
    expected_set = set(range(a + 1, b))
    actual_set = set(t[40:43])
    missing_set = expected_set - actual_set
    s = sum(missing_set)
    if not missing_set:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]