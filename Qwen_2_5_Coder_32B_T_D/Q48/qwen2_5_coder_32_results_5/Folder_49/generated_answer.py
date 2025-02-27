def return_binary_or_hexa(t):
    a, b = (t[80], t[200])
    s = set(t[80:201])
    summ = sum((x for x in range(a + 1, b) if x not in s))
    if summ == 0:
        return ''
    elif summ % 2 == 1:
        return bin(summ)[2:]
    else:
        return hex(summ)[2:]