def return_binary_or_hexa(t):
    a = t[36]
    b = t[54]
    s = set(t[36:55])
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