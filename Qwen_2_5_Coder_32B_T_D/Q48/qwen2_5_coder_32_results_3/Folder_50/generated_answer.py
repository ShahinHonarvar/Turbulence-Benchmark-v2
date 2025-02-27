def return_binary_or_hexa(t):
    a = t[13]
    b = t[76]
    s = 0
    for i in range(a + 1, b):
        if i not in t[14:76]:
            s += i
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    return hex(s)[2:]