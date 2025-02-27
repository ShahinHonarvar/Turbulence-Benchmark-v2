def return_binary_or_hexa(t):
    a = t[56]
    b = t[90]
    s = 0
    p = set(t[57:90])
    for i in range(a + 1, b):
        if i not in p:
            s += i
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]