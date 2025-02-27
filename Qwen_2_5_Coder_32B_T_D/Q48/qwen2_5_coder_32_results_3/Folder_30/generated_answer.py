def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    s = 0
    present = set(t[22:25])
    for i in range(a + 1, b):
        if i not in present:
            s += i
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()