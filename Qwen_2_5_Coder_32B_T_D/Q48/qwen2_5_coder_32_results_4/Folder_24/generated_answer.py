def return_binary_or_hexa(t):
    a, b = (t[13], t[91])
    s = 0
    p = set(t[14:91])
    for n in range(a + 1, b):
        if n not in p:
            s += n
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]