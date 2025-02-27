def return_binary_or_hexa(t):
    a, b = (t[36], t[85])
    if b - a <= 2:
        return ''
    s = sum(range(a + 1, b))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()