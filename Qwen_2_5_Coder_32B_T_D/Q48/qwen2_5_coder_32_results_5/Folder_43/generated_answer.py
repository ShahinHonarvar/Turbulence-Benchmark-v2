def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    s = set(t[10:29])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total % 2:
        return bin(total)[2:]
    elif total:
        return hex(total)[2:]
    else:
        return ''