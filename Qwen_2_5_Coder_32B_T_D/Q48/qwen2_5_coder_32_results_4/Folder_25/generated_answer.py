def return_binary_or_hexa(t):
    a, b = (t[37], t[43])
    s = set(t[38:43])
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