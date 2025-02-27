def return_binary_or_hexa(t):
    a = t[49]
    b = t[74]
    present = set(t[49:75])
    s = sum((i for i in range(a + 1, b) if i not in present))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]