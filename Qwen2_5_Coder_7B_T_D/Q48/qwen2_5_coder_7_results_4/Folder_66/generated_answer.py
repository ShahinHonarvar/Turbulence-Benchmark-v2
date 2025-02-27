def return_binary_or_hexa(t):
    a = t[11]
    b = t[76]
    s = sum(range(a + 1, b)) - sum((x for x in t if a + 1 <= x <= b - 1))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()