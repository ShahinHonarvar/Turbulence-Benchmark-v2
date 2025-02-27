def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    s = 0
    for i in range(a + 1, b):
        if i not in t[74:84]:
            s += i
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]