def return_binary_or_hexa(input_tuple):
    a, *_, b = input_tuple
    missing_sum = sum(set(range(a + 1, b)).difference(input_tuple[1:b]))
    base = binary if missing_sum % 2 else hex
    format_func = '{:0{}b}'.format if base == binary else '{:0{}X}'.format
    return format_func(missing_sum, len(str(missing_sum)))