def return_binary_or_hexa(t):
    a, b = (t[10], t[97])
    total = sum(range(a + 1, b)) - sum((x for x in t if a + 1 <= x <= b - 1))
    if total % 2 == 1:
        return bin(total)[2:]
    elif total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return ''