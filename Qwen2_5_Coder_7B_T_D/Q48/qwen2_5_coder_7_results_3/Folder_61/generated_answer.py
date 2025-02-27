def return_binary_or_hexa(t):
    a, b = (t[0], t[8])
    sum_val = sum((i for i in range(a + 1, b) if i not in t))
    if sum_val % 2 == 0:
        return format(sum_val, 'x')
    else:
        return format(sum_val, 'b')