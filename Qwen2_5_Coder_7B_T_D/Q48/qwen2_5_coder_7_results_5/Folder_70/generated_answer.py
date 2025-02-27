def return_binary_or_hexa(t):
    a = t[43]
    b = t[70]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[a + 1:b]))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')