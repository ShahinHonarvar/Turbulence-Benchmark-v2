def return_binary_or_hexa(t):
    a = t[0]
    b = t[4]
    s = 0
    for i in range(a + 1, b):
        if i not in t:
            s += i
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:]