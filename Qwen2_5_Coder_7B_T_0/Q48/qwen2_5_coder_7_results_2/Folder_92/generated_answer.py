def return_binary_or_hexa(t):
    a, b = (t[0], t[2])
    s = sum(range(a + 1, b))
    if s in t[a + 1:b]:
        return ''
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]