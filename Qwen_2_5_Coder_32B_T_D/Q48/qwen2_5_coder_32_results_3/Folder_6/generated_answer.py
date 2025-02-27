def return_binary_or_hexa(t):
    a = t[20]
    b = t[93]
    s = 0
    expected = set(range(a + 1, b))
    actual = set(t[21:93])
    missing = expected - actual
    if missing:
        s = sum(missing)
        if s % 2:
            return bin(s)[2:]
        else:
            return hex(s)[2:]
    return ''