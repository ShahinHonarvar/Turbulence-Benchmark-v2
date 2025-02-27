def return_binary_or_hexa(t):
    a, b = (t[18], t[52])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[a + 1:b]))
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x').upper()