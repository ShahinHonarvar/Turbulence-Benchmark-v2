def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    s = 0
    expected = set(range(a + 1, b))
    present = set(t[36:64])
    missing = expected - present
    for num in missing:
        s += num
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]