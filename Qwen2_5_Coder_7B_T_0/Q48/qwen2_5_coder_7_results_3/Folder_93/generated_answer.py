def return_binary_or_hexa(t):
    a = t[57]
    b = t[85]
    s = sum((i for i in range(a + 1, b) if i not in t[57:86]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()