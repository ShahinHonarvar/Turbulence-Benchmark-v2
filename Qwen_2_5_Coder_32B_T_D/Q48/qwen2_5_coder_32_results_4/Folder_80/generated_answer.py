def return_binary_or_hexa(tup):
    a = tup[57]
    b = tup[84]
    s = set(tup[58:84])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    elif total > 0:
        return hex(total)[2:]
    else:
        return ''