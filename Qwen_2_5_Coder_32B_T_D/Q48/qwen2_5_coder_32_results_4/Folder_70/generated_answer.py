def return_binary_or_hexa(t):
    a, b = (t[43], t[70])
    s = 0
    for x in range(a + 1, b):
        if x not in t[44:70]:
            s += x
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]