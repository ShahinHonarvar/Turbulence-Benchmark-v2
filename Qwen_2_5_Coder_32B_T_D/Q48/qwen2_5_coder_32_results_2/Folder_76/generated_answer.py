def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    s = 0
    p = set(t[451:905])
    for i in range(a + 1, b):
        if i not in p:
            s += i
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    return hex(s)[2:]