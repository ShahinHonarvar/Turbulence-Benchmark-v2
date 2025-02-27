def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[16], int_tuple[87])
    missing_sum = sum(set(range(a + 1, b)) - set(int_tuple[16:87 + 1]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'X')