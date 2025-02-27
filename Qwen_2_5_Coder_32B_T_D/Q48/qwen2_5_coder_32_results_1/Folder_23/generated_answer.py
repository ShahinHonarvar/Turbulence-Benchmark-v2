def return_binary_or_hexa(t):
    a, b = (t[20], t[36])
    s = set(t[20:37])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()