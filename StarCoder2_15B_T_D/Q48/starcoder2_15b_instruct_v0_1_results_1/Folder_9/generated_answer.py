def return_binary_or_hexa(t):
    a = t[70]
    b = t[200]
    s = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in t:
            s -= i
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()