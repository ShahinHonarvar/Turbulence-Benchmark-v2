def return_binary_or_hexa(t):
    a, _, _, _, b = t[:5]
    s = sum((x for x in range(a + 1, b) if x not in t))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]