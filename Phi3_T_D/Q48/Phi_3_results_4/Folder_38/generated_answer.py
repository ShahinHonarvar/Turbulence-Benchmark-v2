def return_binary_or_hexa(num_tuple):
    a = sorted(set(num_tuple[36:86]))[1]
    b = sorted(set(num_tuple[36:86]))[-2]
    missing_sum = sum(set(range(a + 1, b)) - set(num_tuple[36:86]))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')