def return_binary_or_hexa(t):
    a, b = (t[55], t[84])
    s = 0
    for n in range(a + 1, b):
        if n not in t[55:85]:
            s += n
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]