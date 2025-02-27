def return_binary_or_hexa(t):
    a, b = (t[32], t[44])
    s = sum((x for x in range(a + 1, b) if x not in t[33:44]))
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()