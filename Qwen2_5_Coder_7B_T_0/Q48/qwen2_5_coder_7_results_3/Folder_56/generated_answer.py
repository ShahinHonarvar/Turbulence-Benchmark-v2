def return_binary_or_hexa(t):
    a, b = (t[7], t[9])
    s = sum((i for i in range(a + 1, b) if i not in t[7:9]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()