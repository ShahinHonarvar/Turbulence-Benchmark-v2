def return_binary_or_hexa(t):
    a = t[32]
    b = t[44]
    s = sum((i for i in range(a + 1, b) if i not in t[32:45]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()