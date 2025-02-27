def return_binary_or_hexa(t):
    a, b = (t[44], t[67])
    s = sum((i for i in range(a + 1, b) if i not in t[45:67]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper()