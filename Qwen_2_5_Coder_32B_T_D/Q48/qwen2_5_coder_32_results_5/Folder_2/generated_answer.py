def return_binary_or_hexa(t):
    a, b = (t[72], t[93])
    s = 0
    for x in range(a + 1, b):
        if x not in t[72:94]:
            s += x
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:]