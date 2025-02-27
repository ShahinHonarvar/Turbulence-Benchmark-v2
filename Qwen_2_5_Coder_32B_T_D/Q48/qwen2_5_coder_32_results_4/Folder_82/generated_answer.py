def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[200]
    s = set(tup[21:200])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total == 0:
        return ''
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]