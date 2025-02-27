def return_binary_or_hexa(tup):
    a = tup[60]
    b = tup[90]
    expected = set(range(a + 1, b))
    present = set(tup[61:90])
    missing = expected - present
    if not missing:
        return ''
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:]