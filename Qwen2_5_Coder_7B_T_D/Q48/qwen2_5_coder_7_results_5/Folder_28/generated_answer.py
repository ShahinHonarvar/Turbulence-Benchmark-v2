def return_binary_or_hexa(t):
    a, b = (t[86], t[99])
    s = sum(range(a + 1, b)) - sum((i for i in range(a + 1, b) if i in t[a + 1:b]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()