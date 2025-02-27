def return_binary_or_hexa(t):
    a, b = (t[200], t[202])
    s = sum(range(a + 1, b))
    if any((s - i in t for i in range(a + 1, b))):
        return ''
    s += a + b
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper()