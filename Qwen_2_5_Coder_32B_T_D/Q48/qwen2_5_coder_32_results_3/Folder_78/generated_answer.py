def return_binary_or_hexa(t):
    a, b = (t[62], t[96])
    s = 0
    for i in range(a + 1, b):
        if i not in t[63:96]:
            s += i
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]