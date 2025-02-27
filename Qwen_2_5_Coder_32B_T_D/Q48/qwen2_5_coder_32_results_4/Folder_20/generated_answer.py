def return_binary_or_hexa(t):
    a, b = (t[27], t[96])
    s = set(t[27:97])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total == 0:
        return ''
    elif total % 2 == 1:
        return format(total, 'b')
    else:
        return format(total, 'x')