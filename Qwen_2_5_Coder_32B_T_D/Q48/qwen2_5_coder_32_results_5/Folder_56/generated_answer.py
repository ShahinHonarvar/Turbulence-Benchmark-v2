def return_binary_or_hexa(t):
    a, b = (t[7], t[9])
    s = sum((x for x in range(a + 1, b) if x not in t[8:9]))
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]