def return_binary_or_hexa(t):
    a, b = (t[2], t[7])
    s = sum((x for x in range(a + 1, b) if x not in t[2:8]))
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:]