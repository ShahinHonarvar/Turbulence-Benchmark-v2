def return_binary_or_hexa(t):
    a, b = (t[1], t[8])
    s = sum((x for x in range(a + 1, b) if x not in t[1:9]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]