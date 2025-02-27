def return_binary_or_hexa(t):
    a, b = (t[0], t[10])
    missing_sum = sum(set(range(a + 1, b)).difference(t[:11]))
    if missing_sum % 2 == 0:
        return '{:X}'.format(missing_sum)
    else:
        return format(missing_sum, 'b')