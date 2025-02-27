def return_binary_or_hexa(t):
    a, b = (t[7], t[9])
    s = 0
    for x in range(a + 1, b):
        if x not in t[8:9]:
            s += x
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:].lower()