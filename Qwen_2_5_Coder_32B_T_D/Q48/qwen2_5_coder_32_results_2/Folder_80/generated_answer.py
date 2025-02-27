def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    s = sum(set(range(a + 1, b)) - set(t[58:84]))
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]