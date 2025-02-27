def return_binary_or_hexa(t):
    a, b = (t[36], t[85])
    s = 0
    for x in range(a + 1, b):
        if x not in t[37:85]:
            s += x
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]