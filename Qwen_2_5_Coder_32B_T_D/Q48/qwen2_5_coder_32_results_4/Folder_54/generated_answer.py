def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    s = set(t[35:65])
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