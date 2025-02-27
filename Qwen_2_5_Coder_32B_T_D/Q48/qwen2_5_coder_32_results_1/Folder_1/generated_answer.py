def return_binary_or_hexa(t):
    a, b = (t[17], t[88])
    s = sum((x for x in range(a + 1, b) if x not in t[18:88]))
    if s == 0:
        return ''
    elif s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]