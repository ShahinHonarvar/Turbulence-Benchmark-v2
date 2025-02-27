def return_binary_or_hexa(t):
    a, b = (t[55], t[84])
    s = 0
    for i in range(a + 1, b):
        if i not in t[56:84]:
            s += i
    if s == 0:
        return ''
    elif s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]