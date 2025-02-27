def return_binary_or_hexa(t):
    a, b = (t[933], t[996])
    s = set(t[934:996])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    return ''