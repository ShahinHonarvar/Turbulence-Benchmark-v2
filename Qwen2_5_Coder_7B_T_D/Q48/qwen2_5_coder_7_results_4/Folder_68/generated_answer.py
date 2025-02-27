def return_binary_or_hexa(t):
    a, b = (t[0], t[9])
    total_sum = sum((i for i in range(a + 1, b) if i not in t[1:9]))
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')