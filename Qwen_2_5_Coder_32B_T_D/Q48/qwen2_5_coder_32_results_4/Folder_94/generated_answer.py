def return_binary_or_hexa(t):
    a, b = (t[42], t[87])
    s = 0
    m = set(t[43:87])
    for x in range(a + 1, b):
        if x not in m:
            s += x
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper()