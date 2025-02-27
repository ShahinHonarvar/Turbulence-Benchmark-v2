def return_binary_or_hexa(t):
    a, b = (t[2], t[5])
    s = sum((x for x in range(a + 1, b) if x not in t[2:6]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]