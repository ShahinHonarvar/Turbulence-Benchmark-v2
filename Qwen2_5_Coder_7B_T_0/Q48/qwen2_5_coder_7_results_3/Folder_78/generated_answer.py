def return_binary_or_hexa(t):
    a = t[62]
    b = t[96]
    s = sum((i for i in range(a + 1, b) if i not in t[62:97]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()