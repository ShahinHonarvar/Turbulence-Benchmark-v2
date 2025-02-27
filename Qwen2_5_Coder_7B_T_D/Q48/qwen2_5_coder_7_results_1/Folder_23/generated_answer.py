def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in t[20:37]]
    total -= sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()