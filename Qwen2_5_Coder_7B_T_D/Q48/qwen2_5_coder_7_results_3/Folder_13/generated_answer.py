def return_binary_or_hexa(t):
    a, b = (t[46], t[91])
    sum_val = sum(range(a + 1, b))
    missing_ints = [i for i in range(a + 1, b) if i not in t[a + 1:b]]
    if sum_val % 2 == 0:
        return format(sum_val, 'x')
    else:
        return format(sum_val, 'b')