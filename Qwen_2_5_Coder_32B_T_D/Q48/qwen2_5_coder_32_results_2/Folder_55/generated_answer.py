def return_binary_or_hexa(t):
    a, b = (t[10], t[12])
    s = sum((x for x in range(a + 1, b) if x not in t[10:13]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()