def return_binary_or_hexa(t):
    a = t[29]
    b = t[53]
    s = sum(range(a + 1, b)) - sum((t[i] for i in range(29, 54)))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()