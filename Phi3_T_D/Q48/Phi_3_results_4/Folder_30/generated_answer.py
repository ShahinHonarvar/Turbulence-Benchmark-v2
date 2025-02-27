def return_binary_or_hexa(t):
    a, b = (t[22], t[24])
    missing_sum = sum(set(range(a + 1, b)).difference(t[22:24]))
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')