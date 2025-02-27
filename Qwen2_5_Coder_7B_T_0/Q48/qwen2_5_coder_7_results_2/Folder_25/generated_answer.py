def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    s = sum((i for i in range(a + 1, b) if i not in t[a + 1:b]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()