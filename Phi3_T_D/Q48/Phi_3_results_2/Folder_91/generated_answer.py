def return_binary_or_hexa(input_tuple):
    a, b = (input_tuple[0], input_tuple[6])
    missing_sum = sum(set(range(a + 1, b)).difference(input_tuple))
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')