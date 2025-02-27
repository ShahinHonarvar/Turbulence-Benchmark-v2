def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    s = sum((i for i in range(a + 1, b) if i not in t[a + 1:b - 1]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]