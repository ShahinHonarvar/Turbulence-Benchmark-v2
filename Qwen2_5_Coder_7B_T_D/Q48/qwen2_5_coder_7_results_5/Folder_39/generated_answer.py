def return_binary_or_hexa(t):
    a, b = (t[44], t[91])
    s = sum((i for i in range(a + 1, b) if i not in t[44:92]))
    if s % 2 == 1:
        return format(s, 'b')
    else:
        return format(s, 'x').upper()