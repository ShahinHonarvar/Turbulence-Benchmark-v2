def return_binary_or_hexa(t):
    a, b = (t[11], t[76])
    s = sum((n for n in range(a + 1, b) if n not in t[12:76]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]