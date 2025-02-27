def return_binary_or_hexa(values):
    a = values[60]
    b = values[90]
    missing_sum = sum((i for i in range(a + 1, b) if i not in values[60:90]))
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')