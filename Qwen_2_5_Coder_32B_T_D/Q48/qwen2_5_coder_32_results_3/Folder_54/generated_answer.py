def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    s = 0
    for x in range(a + 1, b):
        if x not in t[35:65]:
            s += x
    if s == 0:
        return ''
    elif s % 2 == 1:
        return format(s, 'b')
    else:
        return format(s, 'x')