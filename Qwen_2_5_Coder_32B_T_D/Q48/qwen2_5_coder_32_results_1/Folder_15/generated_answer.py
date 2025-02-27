def return_binary_or_hexa(t):
    a, b = (t[0], t[4])
    s = set(t[:5])
    total = 0
    for x in range(a + 1, b):
        if x not in s:
            total += x
    if total == 0:
        return ''
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]