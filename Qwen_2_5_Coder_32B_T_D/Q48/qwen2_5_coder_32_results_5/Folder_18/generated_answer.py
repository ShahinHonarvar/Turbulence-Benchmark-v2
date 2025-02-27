def return_binary_or_hexa(t):
    a = t[56]
    b = t[90]
    s = sum((x for x in range(a + 1, b) if x not in t[57:90]))
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]