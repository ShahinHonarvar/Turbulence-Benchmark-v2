def return_binary_or_hexa(t):
    a = t[18]
    b = t[60]
    total_sum = sum((i for i in range(a + 1, b) if i not in t[a:b + 1]))
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')