def return_binary_or_hexa(t):
    a = t[33]
    b = t[78]
    s = set(t[34:78])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]