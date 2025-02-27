def return_binary_or_hexa(t):
    a, b = (t[6], t[9])
    s = 0
    for x in range(a + 1, b):
        if x not in t[7:9]:
            s += x
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]