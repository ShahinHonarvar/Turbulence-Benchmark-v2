def return_binary_or_hexa(t):
    a = t[2]
    b = t[8]
    s = sum((i for i in range(a + 1, b) if i not in t[a + 1:b]))
    if s % 2 == 0:
        return format(s, 'x')
    else:
        return format(s, 'b')