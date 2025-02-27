def return_binary_or_hexa(t):
    a = t[20]
    b = t[93]
    s = 0
    m = set(t[21:93])
    for x in range(a + 1, b):
        if x not in m:
            s += x
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]