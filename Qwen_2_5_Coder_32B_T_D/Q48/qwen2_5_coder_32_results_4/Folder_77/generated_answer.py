def return_binary_or_hexa(t):
    a, b = (t[18], t[52])
    s = 0
    for i in range(a + 1, b):
        if i not in t[19:52]:
            s += i
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]