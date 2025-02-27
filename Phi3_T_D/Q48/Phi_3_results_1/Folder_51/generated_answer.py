def return_binary_or_hexa(input_tuple):
    a, b = (input_tuple[6], input_tuple[9])
    missing_numbers_sum = sum(range(a + 1, b)) - sum(input_tuple[6:10])
    if missing_numbers_sum == 0:
        return ''
    return '{:b}'.format(missing_numbers_sum) if missing_numbers_sum % 2 else '{:x}'.format(missing_numbers_sum)