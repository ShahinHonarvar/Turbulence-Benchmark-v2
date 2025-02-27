def return_binary_or_hexa(t):
    a, b = (t[38], t[81])
    s = sum((i for i in range(a + 1, b) if i not in t[a:b]))
    return format(s, 'b') if s % 2 else format(s, 'x')