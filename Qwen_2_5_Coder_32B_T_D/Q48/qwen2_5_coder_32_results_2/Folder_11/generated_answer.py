def return_binary_or_hexa(t):
    a = t[48]
    b = t[76]
    s = 0
    for i in range(a + 1, b):
        if i not in t[49:76]:
            s += i
    if s % 2 == 1:
        return bin(s)[2:]
    elif s % 2 == 0 and s != 0:
        return hex(s)[2:]
    else:
        return ''