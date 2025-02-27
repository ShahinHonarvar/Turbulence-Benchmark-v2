def return_binary_or_hexa(input_tuple: tuple) -> str:
    a = input_tuple[57]
    b = input_tuple[84]
    expected_range = set(range(a + 1, b))
    actual_range = set(input_tuple[a + 1:b])
    missing_numbers = expected_range - actual_range
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:]