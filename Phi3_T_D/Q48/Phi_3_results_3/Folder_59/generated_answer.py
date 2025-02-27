def return_binary_or_hexa(t):
    a = t[0]
    b = t[10]
    missing_sum = sum((x for x in range(a + 1, b) if x not in t[1:10]))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')