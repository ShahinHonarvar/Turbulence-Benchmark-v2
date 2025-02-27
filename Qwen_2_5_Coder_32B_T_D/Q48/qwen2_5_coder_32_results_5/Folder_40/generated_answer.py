def return_binary_or_hexa(t):
    a, _, _, b = t[:4]
    s = sum((i for i in range(a + 1, b) if i not in t[:4]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]