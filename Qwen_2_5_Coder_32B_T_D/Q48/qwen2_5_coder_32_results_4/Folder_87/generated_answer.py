def return_binary_or_hexa(t):
    a, b = (t[20], t[43])
    s = 0
    m = set(t[20:44])
    for i in range(a + 1, b):
        if i not in m:
            s += i
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]