def return_binary_or_hexa(t):
    a = t[36]
    b = t[85]
    s = sum(range(a + 1, b)) - sum((t[i] for i in range(37, 85)))
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]