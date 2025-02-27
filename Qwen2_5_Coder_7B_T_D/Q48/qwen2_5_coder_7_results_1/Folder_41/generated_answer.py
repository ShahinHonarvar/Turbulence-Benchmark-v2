def return_binary_or_hexa(t):
    a, b = (t[3], t[8])
    total = sum((i for i in range(a + 1, b) if i not in t[3:9]))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()