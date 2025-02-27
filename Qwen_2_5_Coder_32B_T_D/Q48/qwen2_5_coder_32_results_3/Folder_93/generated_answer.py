def return_binary_or_hexa(t):
    a, b = (t[57], t[85])
    r = set(t[58:85])
    s = sum((x for x in range(a + 1, b) if x not in r))
    if s:
        return bin(s)[2:] if s % 2 else hex(s)[2:]
    return ''