def return_binary_or_hexa(my_tuple):
    a = my_tuple[39]
    b = my_tuple[43]
    expected_range = set(range(a + 1, b))
    actual_range = set(my_tuple[a + 1:b])
    missing_numbers = expected_range - actual_range
    if len(missing_numbers) == 0:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:]
    return bin(sum_of_missing_numbers)[2:]