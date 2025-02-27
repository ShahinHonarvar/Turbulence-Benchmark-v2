def return_binary_or_hexa(t):
    a, b = (t[46], t[91])
    s = sum((x for x in range(a + 1, b) if x not in t[47:91]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]