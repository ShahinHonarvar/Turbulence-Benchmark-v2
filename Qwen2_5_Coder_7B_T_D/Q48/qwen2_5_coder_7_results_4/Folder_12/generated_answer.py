def return_binary_or_hexa(t):
    a = t[16]
    b = t[87]
    total = sum(range(a + 1, b))
    missing = [x for x in range(a + 1, b) if x not in t[a + 1:b]]
    if missing == list(range(a + 1, b)):
        return ''
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()