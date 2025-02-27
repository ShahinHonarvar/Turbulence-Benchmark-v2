def return_binary_or_hexa(tup):
    a, b = (tup[30], tup[200])
    if a >= b - 1:
        return ''
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in tup[30:201]]
    total -= sum(missing)
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]