def return_binary_or_hexa(t):
    a, _, b = t[:3]
    s = sum((i for i in range(a + 1, b) if i not in t))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:].lower()