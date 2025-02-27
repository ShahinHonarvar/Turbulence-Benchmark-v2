def return_binary_or_hexa(t):
    a = t[81]
    b = t[86]
    sum_val = sum((i for i in range(a + 1, b) if i not in t))
    if sum_val % 2 == 0:
        return format(sum_val, 'x')
    else:
        return format(sum_val, 'b')