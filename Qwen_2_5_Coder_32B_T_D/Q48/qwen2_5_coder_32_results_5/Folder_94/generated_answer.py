def return_binary_or_hexa(t):
    a, b = (t[42], t[87])
    s = set(t[42:88])
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