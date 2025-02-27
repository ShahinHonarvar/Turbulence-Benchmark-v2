def return_binary_or_hexa(t):
    a = t[32]
    b = t[44]
    s = 0
    present = set(t[33:44])
    for i in range(a + 1, b):
        if i not in present:
            s += i
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]