def return_binary_or_hexa(t):
    a, b = (t[69], t[97])
    s = 0
    for x in range(a + 1, b):
        if x not in t[70:97]:
            s += x
    if s == 0:
        return ''
    if s % 2 == 1:
        return format(s, 'b')
    else:
        return format(s, 'x')