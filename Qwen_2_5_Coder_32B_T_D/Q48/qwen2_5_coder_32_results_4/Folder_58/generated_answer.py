def return_binary_or_hexa(t):
    a, b = (t[275], t[871])
    s = set(t[275:872])
    p = sum((x for x in range(a + 1, b) if x not in s))
    if p == 0:
        return ''
    if p % 2:
        return bin(p)[2:]
    else:
        return hex(p)[2:]