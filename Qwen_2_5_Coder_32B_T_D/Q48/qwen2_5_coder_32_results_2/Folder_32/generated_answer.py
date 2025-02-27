def return_binary_or_hexa(t):
    a, b = (t[86], t[90])
    s = sum((i for i in range(a + 1, b) if i not in t[86:91]))
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]