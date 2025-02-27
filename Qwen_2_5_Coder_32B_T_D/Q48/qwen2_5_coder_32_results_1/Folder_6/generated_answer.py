def return_binary_or_hexa(t):
    a, b = (t[20], t[93])
    s = set(t[20:94])
    tot = 0
    for i in range(a + 1, b):
        if i not in s:
            tot += i
    if tot == 0:
        return ''
    elif tot % 2 == 1:
        return bin(tot)[2:]
    else:
        return hex(tot)[2:]