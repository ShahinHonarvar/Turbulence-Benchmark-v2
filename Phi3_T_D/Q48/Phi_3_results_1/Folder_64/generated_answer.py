def return_binary_or_hexa(t):
    a = t[0]
    b = t[5]
    present = set(t)
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total == 0:
        return ''
    if total % 2:
        return format(total, 'b')
    return format(total, 'x')