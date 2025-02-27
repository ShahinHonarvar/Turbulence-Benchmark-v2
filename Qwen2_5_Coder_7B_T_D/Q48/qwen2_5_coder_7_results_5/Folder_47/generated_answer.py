def return_binary_or_hexa(t):
    a = t[29]
    b = t[53]
    s = sum((i for i in range(a + 1, b) if i not in t[a + 1:b]))
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]