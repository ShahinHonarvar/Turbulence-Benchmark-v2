def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[49], int_tuple[74])
    sum_excluded = sum((i for i in range(a + 1, b) if i not in int_tuple[49:75]))
    if sum_excluded % 2:
        return format(sum_excluded, 'b')
    elif sum_excluded > 0:
        return format(sum_excluded, 'x')
    return ''