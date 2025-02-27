def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[12]
    expected_set = set(range(a + 1, b))
    actual_set = set(tup[11:12])
    missing_set = expected_set - actual_set
    s = sum(missing_set)
    if not missing_set:
        return ''
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:]