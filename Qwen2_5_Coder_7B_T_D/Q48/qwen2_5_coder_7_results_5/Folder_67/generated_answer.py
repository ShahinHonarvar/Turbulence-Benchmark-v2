def return_binary_or_hexa(t):
    a = t[44]
    b = t[67]
    s = sum(range(a + 1, b)) - sum((t[i] for i in range(44, 68)))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()