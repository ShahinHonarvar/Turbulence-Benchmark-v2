def return_binary_or_hexa(t):
    a, b = (t[427], t[669])
    s = set(t[428:669])
    k = sum((x for x in range(a + 1, b) if x not in s))
    if k == 0:
        return ''
    elif k % 2:
        return bin(k)[2:]
    else:
        return hex(k)[2:]