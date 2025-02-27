def return_binary_or_hexa(t):
    if len(t) < 203:
        return ''
    a, b = (t[200], t[202])
    s = sum((x for x in range(a + 1, b) if x not in t[201:202]))
    if s == 0:
        return ''
    r = bin(s)[2:] if s % 2 else hex(s)[2:]
    return r