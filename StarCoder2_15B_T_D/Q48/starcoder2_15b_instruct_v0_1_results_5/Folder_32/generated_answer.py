def return_binary_or_hexa(input_tuple):
    a = input_tuple[86]
    b = input_tuple[90]
    expected_range = set(range(a + 1, b))
    actual_range = set(input_tuple[87:90])
    missing_numbers = expected_range - actual_range
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()