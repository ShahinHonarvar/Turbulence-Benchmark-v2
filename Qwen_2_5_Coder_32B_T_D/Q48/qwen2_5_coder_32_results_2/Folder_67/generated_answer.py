def return_binary_or_hexa(t):
    a, b = (t[44], t[67])
    s = 0
    p = set(t[44:68])
    for i in range(a + 1, b):
        if i not in p:
            s += i
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]