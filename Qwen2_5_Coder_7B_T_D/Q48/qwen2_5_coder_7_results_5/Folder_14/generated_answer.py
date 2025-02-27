def return_binary_or_hexa(t):
    a = t[2]
    b = t[5]
    s = sum((i for i in range(a + 1, b) if i not in t[a:b + 1]))
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]