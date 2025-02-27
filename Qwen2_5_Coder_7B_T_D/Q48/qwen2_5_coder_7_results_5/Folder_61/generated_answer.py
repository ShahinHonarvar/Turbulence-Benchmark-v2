def return_binary_or_hexa(t):
    a, b = (t[0], t[8])
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in t]
    if missing == list(range(a + 1, b)):
        return ''
    else:
        total -= sum(missing)
        if total % 2 == 1:
            return bin(total)[2:]
        else:
            return hex(total)[2:].upper()