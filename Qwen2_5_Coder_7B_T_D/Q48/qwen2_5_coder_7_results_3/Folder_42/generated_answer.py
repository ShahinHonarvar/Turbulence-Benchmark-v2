def return_binary_or_hexa(t):
    a = t[18]
    b = t[60]
    s = sum((i for i in range(a + 1, b) if i not in set(t[a + 1:b])))
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]