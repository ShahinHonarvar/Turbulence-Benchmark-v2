def return_binary_or_hexa(t):
    a, _, _, _, _, b = t[:6]
    s = set(t[:6])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]