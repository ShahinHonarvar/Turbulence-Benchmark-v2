def return_binary_or_hexa(t):
    a, b = (t[32], t[99])
    s = 0
    ct = set(t[33:99])
    for i in range(a + 1, b):
        if i not in ct:
            s += i
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]