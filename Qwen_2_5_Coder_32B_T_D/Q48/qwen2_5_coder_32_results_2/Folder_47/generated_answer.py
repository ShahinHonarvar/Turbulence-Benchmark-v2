def return_binary_or_hexa(t):
    a, b = (t[29], t[53])
    s = set(t[29:54])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total == 0:
        return ''
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:]