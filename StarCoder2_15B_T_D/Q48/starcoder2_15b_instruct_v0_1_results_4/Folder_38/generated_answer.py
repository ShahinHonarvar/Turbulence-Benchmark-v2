def return_binary_or_hexa(t):
    a = t[36]
    b = t[85]
    s = sum([i for i in range(a + 1, b) if i not in t])
    return bin(s)[2:] if s % 2 else hex(s)[2:]