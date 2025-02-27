def return_binary_or_hexa(t):
    a = t[275]
    b = t[871]
    missing = set(range(a + 1, b)) - set(t[276:871])
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]