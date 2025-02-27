def return_binary_or_hexa(t):
    a, b = (t[48], t[76])
    s = set(t[48:77])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total % 2:
        return bin(total)[2:]
    elif total > 0:
        return hex(total)[2:]
    return ''