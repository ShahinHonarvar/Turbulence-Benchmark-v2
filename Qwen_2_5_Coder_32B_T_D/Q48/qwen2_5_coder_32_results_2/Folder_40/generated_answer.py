def return_binary_or_hexa(t):
    a, _, _, b = t[:4]
    s = set(t)
    total = sum((x for x in range(a + 1, b) if x not in s))
    if total == 0:
        return ''
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:]