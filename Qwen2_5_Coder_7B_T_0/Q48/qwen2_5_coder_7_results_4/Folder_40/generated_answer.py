def return_binary_or_hexa(t):
    a, b = (t[0], t[3])
    s = sum((i for i in range(a + 1, b) if i not in t[1:3]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()