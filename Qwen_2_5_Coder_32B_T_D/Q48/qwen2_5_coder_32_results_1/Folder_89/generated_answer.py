def return_binary_or_hexa(t):
    a, b = (t[55], t[84])
    s = 0
    d = set(t[55:85])
    for i in range(a + 1, b):
        if i not in d:
            s += i
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]