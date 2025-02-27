def return_binary_or_hexa(input_tuple):
    a = input_tuple[15]
    b = input_tuple[57]
    excluded_nums_set = set(input_tuple[15:57 + 1])
    missing_sum = sum((i for i in range(a + 1, b, 1) if i not in excluded_nums_set))
    if missing_sum % 2 == 0:
        return '{:X}'.format(missing_sum)
    else:
        return '{:b}'.format(missing_sum)