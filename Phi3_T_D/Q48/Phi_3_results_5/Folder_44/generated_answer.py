def return_binary_or_hexa(data_tuple):
    a = data_tuple[36]
    b = data_tuple[52]
    expected_range = set(range(a + 1, b))
    actual_range = set(data_tuple[36:53])
    missing_numbers = expected_range - actual_range
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:]