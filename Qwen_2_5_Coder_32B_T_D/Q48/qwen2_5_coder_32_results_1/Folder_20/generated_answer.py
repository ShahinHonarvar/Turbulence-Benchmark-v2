def return_binary_or_hexa(t):
    a, b = (t[27], t[96])
    s = sum((x for x in range(a + 1, b) if x not in t[28:96]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]