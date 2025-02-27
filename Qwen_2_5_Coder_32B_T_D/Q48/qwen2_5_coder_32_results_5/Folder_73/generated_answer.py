def return_binary_or_hexa(t):
    a = t[10]
    b = t[76]
    s = set(t[11:76])
    summ = sum((x for x in range(a + 1, b) if x not in s))
    if summ == 0:
        return ''
    if summ % 2:
        return bin(summ)[2:]
    return hex(summ)[2:]