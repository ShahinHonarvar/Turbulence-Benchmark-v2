def return_binary_or_hexa(t):
    a = t[56]
    b = t[90]
    s = 0
    m = set(t[57:90])
    for i in range(a + 1, b):
        if i not in m:
            s += i
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:]