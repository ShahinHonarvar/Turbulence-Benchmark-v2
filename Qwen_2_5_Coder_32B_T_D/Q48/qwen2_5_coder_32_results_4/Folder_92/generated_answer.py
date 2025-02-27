def return_binary_or_hexa(t):
    a, _, b = t[:3]
    s = set(t)
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total == 0:
        return ''
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:]