def return_binary_or_hexa(tup):
    a, b = (tup[80], tup[200])
    total_sum = sum(range(a + 1, b))
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')