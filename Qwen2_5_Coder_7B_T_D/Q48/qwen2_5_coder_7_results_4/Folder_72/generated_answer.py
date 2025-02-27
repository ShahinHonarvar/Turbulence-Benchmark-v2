def return_binary_or_hexa(t):
    a, b = (t[13], t[70])
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in t[13:70]]
    if missing:
        total = sum(missing)
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]