def return_binary_or_hexa(t):
    a, b = (t[10], t[97])
    s = 0
    expected = set(range(a + 1, b))
    present = set(t[11:97])
    missing = expected - present
    for num in missing:
        s += num
    if s:
        return bin(s)[2:] if s % 2 else hex(s)[2:]
    return ''