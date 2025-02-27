def return_binary_or_hexa(t):
    a = t[1]
    b = t[4]
    total = sum(range(a + 1, b))
    missing = [x for x in range(a + 1, b) if x not in t[1:4]]
    if total != sum(missing):
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()