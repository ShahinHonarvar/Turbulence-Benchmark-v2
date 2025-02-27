def return_binary_or_hexa(t):
    a, b = (t[2], t[7])
    s = sum(range(a + 1, b))
    if any((x in t and a <= x < b for x in range(a + 1, b))):
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()