def return_binary_or_hexa(t):
    a, b = (t[60], t[90])
    present = set(t[61:90])
    s = sum((x for x in range(a + 1, b) if x not in present))
    if not s:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]