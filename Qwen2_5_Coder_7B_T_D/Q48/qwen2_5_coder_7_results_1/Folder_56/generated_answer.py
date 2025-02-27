def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[7:10]))
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')