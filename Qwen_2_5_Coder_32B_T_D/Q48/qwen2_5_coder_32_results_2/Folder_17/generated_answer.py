def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    expected_set = set(range(a + 1, b))
    actual_set = set(t[74:84])
    missing = expected_set - actual_set
    s = sum(missing)
    if missing:
        if s % 2:
            return bin(s)[2:]
        else:
            return hex(s)[2:]
    else:
        return ''