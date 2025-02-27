def return_binary_or_hexa(t):
    a, b = (t[10], t[97])
    s = set(t[10:98])
    total = 0
    for x in range(a + 1, b):
        if x not in s:
            total += x
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    return hex(total)[2:]