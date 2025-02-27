def return_binary_or_hexa(t):
    a, b = (t[38], t[52])
    s = 0
    p = set(t[39:52])
    for i in range(a + 1, b):
        if i not in p:
            s += i
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]