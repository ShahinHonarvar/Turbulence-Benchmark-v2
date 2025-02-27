def return_binary_or_hexa(t):
    a, b = (t[48], t[76])
    s = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in t[a + 1:b]]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()