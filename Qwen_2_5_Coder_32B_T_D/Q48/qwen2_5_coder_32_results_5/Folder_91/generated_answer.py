def return_binary_or_hexa(t):
    a, _, _, _, _, _, b = t
    s = sum((i for i in range(a + 1, b) if i not in t[1:6]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]