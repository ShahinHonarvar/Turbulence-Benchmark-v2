def return_binary_or_hexa(t):
    a = t[70]
    b = t[200]
    s = set(range(a + 1, b))
    for i in range(70, 201):
        s.discard(t[i])
    if not s:
        return ''
    total = sum(s)
    if total % 2 == 0:
        return format(total, 'x')
    else:
        return format(total, 'b')