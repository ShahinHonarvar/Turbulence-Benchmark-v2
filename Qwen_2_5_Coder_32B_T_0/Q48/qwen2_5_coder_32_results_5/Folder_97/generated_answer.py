def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    s = 0
    for i in range(a + 1, b):
        if i not in t[35:69]:
            s += i
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]