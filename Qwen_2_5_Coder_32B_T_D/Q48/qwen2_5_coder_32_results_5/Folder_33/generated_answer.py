def return_binary_or_hexa(tp):
    a, b = (tp[13], tp[35])
    s = set(tp[14:35])
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