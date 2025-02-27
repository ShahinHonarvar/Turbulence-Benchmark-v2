def return_binary_or_hexa(t):
    a, b = (t[18], t[52])
    s = sum(range(a + 1, b)) - sum((t[i] for i in range(18, 53)))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()