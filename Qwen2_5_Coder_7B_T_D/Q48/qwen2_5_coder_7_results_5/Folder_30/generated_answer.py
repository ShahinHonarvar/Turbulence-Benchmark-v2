def return_binary_or_hexa(tup):
    a, b = (tup[22], tup[24])
    target = set(range(a + 1, b))
    present = set(tup[22:25])
    missing = target - present
    if missing:
        return ''
    else:
        total = sum(missing)
        if total % 2 == 0:
            return hex(total)[2:].upper()
        else:
            return bin(total)[2:]