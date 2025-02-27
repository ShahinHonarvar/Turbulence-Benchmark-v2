def return_binary_or_hexa(t):
    a = t[10]
    b = t[79]
    total = 0
    present = set(t[11:79])
    for i in range(a + 1, b):
        if i not in present:
            total += i
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]