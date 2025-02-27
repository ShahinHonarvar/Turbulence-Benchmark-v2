def return_binary_or_hexa(t):
    a, b = (t[81], t[86])
    s = sum((x for x in range(a + 1, b) if x not in t[82:86]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]