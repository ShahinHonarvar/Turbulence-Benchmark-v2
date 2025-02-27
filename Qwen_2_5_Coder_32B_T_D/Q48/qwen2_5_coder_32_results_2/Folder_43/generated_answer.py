def return_binary_or_hexa(t):
    a, b = (t[10], t[28])
    s = sum((x for x in range(a + 1, b) if x not in t[11:28]))
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    return hex(s)[2:]