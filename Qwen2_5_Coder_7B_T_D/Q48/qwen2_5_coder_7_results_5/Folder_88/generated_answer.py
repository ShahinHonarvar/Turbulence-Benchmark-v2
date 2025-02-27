def return_binary_or_hexa(t):
    a = t[3]
    b = t[9]
    total_sum = sum((i for i in range(a + 1, b) if i not in t))
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')