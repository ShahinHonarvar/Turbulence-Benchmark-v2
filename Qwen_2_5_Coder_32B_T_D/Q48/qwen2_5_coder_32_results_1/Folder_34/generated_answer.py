def return_binary_or_hexa(t):
    a = t[60]
    b = t[200]
    s = set(t[60:201])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    elif total % 2 == 0 and total != 0:
        return hex(total)[2:]
    else:
        return ''