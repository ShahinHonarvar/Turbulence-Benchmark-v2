def return_binary_or_hexa(t):
    a, b = (t[1], t[7])
    s, m = (0, set(t[1:8]))
    for n in range(a + 1, b):
        if n not in m:
            s += n
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]