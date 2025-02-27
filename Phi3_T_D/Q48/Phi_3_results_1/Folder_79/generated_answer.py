def return_binary_or_hexa(tpl):
    a = tpl[1]
    b = tpl[7]
    sum_not_in_tuple = sum((i for i in range(a + 1, b) if i not in tpl[1:8]))
    if sum_not_in_tuple % 2:
        return format(sum_not_in_tuple, 'b')
    else:
        return format(sum_not_in_tuple, 'x')