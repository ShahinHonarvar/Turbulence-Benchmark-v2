def return_binary_or_hexa(t):
    a, b = (t[0], t[10])
    s = sum((x for x in range(a + 1, b) if x not in t))
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]