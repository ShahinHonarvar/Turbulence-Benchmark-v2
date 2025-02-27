def return_binary_or_hexa(t):
    a = t[68]
    b = t[99]
    s = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in t:
            s -= i
    if s & 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()