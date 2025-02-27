def return_binary_or_hexa(t):
    a = t[32]
    b = t[44]
    s = set(t[32:45])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]